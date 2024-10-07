import taichi as ti

ti.init(arch=ti.vulkan)

# Simulation parameters
n_particles = 1000
n_grid = 100

# Spatial and temporal resolution
dx, inv_dx = 1 / n_grid, float(n_grid)  # Grid spacing and its inverse
dt = 1e-4
p_vol, p_rho = (dx * 0.5) ** 2, 1  # Particle volume and density
p_mass = p_vol * p_rho  # Particle mass

# Material properties
E, nu = 5e3, 0.2  # Young's modulus and Poisson's ratio
mu_0, lambda_0 = E / (2 * (1 + nu)), E * nu / ((1 + nu) * (1 - 2 * nu))  # Lame parameters

# Particle fields
x = ti.Vector.field(2, dtype=float, shape=n_particles)  # Particle positions
v = ti.Vector.field(2, dtype=float, shape=n_particles)  # Particle velocities
C = ti.Matrix.field(2, 2, dtype=float, shape=n_particles)  # Affine velocity field
F = ti.Matrix.field(2, 2, dtype=float, shape=n_particles)  # Deformation gradient
Jp = ti.field(dtype=float, shape=n_particles)  # Plastic deformation
grid_v = ti.Vector.field(2, dtype=float, shape=(n_grid, n_grid))  # Grid velocity
grid_m = ti.field(dtype=float, shape=(n_grid, n_grid))  # Grid mass
gravity = ti.Vector.field(2, dtype=float, shape=())  # Gravity vector
attractor_strength = ti.field(dtype=float, shape=())  # Attractor strength
attractor_pos = ti.Vector.field(2, dtype=float, shape=())  # Attractor position

# Water simulation visualization field
water = ti.Vector.field(2, dtype=float, shape=n_particles)  # Visual representation of particles
mouse_circle = ti.Vector.field(2, dtype=float, shape=(1,))  # To visualize mouse interaction


@ti.kernel
def substep():
    # Reset grid velocities and masses
    for i, j in grid_m:
        grid_v[i, j] = [0, 0]  # Clear grid velocities
        grid_m[i, j] = 0  # Clear grid masses

    # Particle to grid (P2G) step
    for p in x:
        base = (x[p] * inv_dx - 0.5).cast(int)  # Determine grid cell for particle
        fx = x[p] * inv_dx - base.cast(float)  # Fractional part for interpolation

        # Quadratic kernel weights for smoother interpolation
        w = [0.5 * (1.5 - fx) ** 2, 0.75 - (fx - 1) ** 2, 0.5 * (fx - 0.5) ** 2]

        # Update deformation gradient
        F[p] = (ti.Matrix.identity(float, 2) + dt * C[p]) @ F[p]

        # Compute hardening coefficient
        h = ti.max(0.1, ti.min(5, ti.exp(10 * (1.0 - Jp[p]))))
        mu, la = mu_0 * h, lambda_0 * h  # Update Lame parameters

        # Set shear modulus to zero for this iteration
        mu = 0.0

        # Perform singular value decomposition (SVD) on deformation gradient
        U, sig, V = ti.svd(F[p])
        J = 1.0
        for d in ti.static(range(2)):
            new_sig = sig[d, d]
            Jp[p] *= sig[d, d] / new_sig  # Update plastic deformation
            sig[d, d] = new_sig
            J *= new_sig  # Compute determinant of F

        F[p] = ti.Matrix.identity(float, 2) * ti.sqrt(J)  # Update deformation gradient
        stress = 2 * mu * (F[p] - U @ V.transpose()) @ F[p].transpose() + ti.Matrix.identity(float, 2) * la * J * (J - 1)
        stress = (-dt * p_vol * 4 * inv_dx * inv_dx) * stress  # Scale stress by time step

        # Compute affine stress
        affine = stress + p_mass * C[p]

        # Loop over the 3x3 grid neighborhood
        for i, j in ti.static(ti.ndrange(3, 3)):
            offset = ti.Vector([i, j])
            dpos = (offset.cast(float) - fx) * dx  # Position offset
            weight = w[i][0] * w[j][1]  # Kernel weight
            grid_v[base + offset] += weight * (p_mass * v[p] + affine @ dpos)  # Update grid velocity
            grid_m[base + offset] += weight * p_mass  # Update grid mass

    # Update grid velocities and apply forces
    for i, j in grid_m:
        if grid_m[i, j] > 0:  # Avoid division by zero
            grid_v[i, j] = (1 / grid_m[i, j]) * grid_v[i, j]  # Convert momentum to velocity
            grid_v[i, j] += dt * gravity[None] * 30  # Apply gravity
            # Compute distance to attractor
            dist = attractor_pos[None] - dx * ti.Vector([i, j])
            grid_v[i, j] += dist / (0.01 + dist.norm()) * attractor_strength[None] * dt * 100  # Apply attractor forces

            # Enforce boundary conditions
            if i < 3 and grid_v[i, j][0] < 0:
                grid_v[i, j][0] = 0
            if i > n_grid - 3 and grid_v[i, j][0] > 0:
                grid_v[i, j][0] = 0
            if j < 3 and grid_v[i, j][1] < 0:
                grid_v[i, j][1] = 0
            if j > n_grid - 3 and grid_v[i, j][1] > 0:
                grid_v[i, j][1] = 0

    # Grid to particle (G2P) step
    for p in x:
        base = (x[p] * inv_dx - 0.5).cast(int)  # Determine grid cell for particle
        fx = x[p] * inv_dx - base.cast(float)  # Fractional part for interpolation
        w = [0.5 * (1.5 - fx) ** 2, 0.75 - (fx - 1.0) ** 2, 0.5 * (fx - 0.5) ** 2]

        new_v = ti.Vector.zero(float, 2)  # Initialize new velocity
        new_C = ti.Matrix.zero(float, 2, 2)  # Initialize new affine velocity

        # Loop over the 3x3 grid neighborhood
        for i, j in ti.static(ti.ndrange(3, 3)):
            dpos = ti.Vector([i, j]).cast(float) - fx  # Compute offset for grid position
            g_v = grid_v[base + ti.Vector([i, j])]  # Get grid velocity
            weight = w[i][0] * w[j][1]  # Compute kernel weight
            new_v += weight * g_v  # Accumulate new velocity
            new_C += 4 * inv_dx * weight * g_v.outer_product(dpos)  # Update affine velocity

        v[p], C[p] = new_v, new_C  # Update particle velocity and affine field
        x[p] += dt * v[p]  # Advection: update particle position based on velocity


@ti.kernel
def reset():
    # Initialize particles
    for i in range(n_particles):
        x[i] = [
            ti.random() * 0.2 + 0.3 + 0.10 * (i // n_particles),  # Random x position
            ti.random() * 0.2 + 0.05 + 0.32 * (i // n_particles),  # Random y position
        ]
        v[i] = [0, 0]  # Set initial velocity to zero
        F[i] = ti.Matrix([[1, 0], [0, 1]])  # Set initial deformation gradient to identity
        Jp[i] = 1  # Initialize plastic deformation to 1
        C[i] = ti.Matrix.zero(float, 2, 2)  # Initialize affine velocity field to zero


@ti.kernel
def render():
    # Render the particle positions to the water field for visualization
    for i in range(n_particles):
        water[i] = x[i]


def main():


    res = (512, 512)
    window = ti.ui.Window("Taichi MLS-MPM-128", res=res, vsync=True)
    canvas = window.get_canvas()
    radius = 0.003

    reset()
    gravity[None] = [0, -1]

    while window.running:
        if window.get_event(ti.ui.PRESS):
            if window.event.key == "r":
                reset()
            elif window.event.key in [ti.ui.ESCAPE]:
                break

        mouse = window.get_cursor_pos()
        mouse_circle[0] = ti.Vector([mouse[0], mouse[1]])
        canvas.circles(mouse_circle, color=(0.2, 0.4, 0.6), radius=0.05)
        attractor_pos[None] = [mouse[0], mouse[1]]
        attractor_strength[None] = 0
        if window.is_pressed(ti.ui.LMB):
            attractor_strength[None] = 1
        if window.is_pressed(ti.ui.RMB):
            attractor_strength[None] = -1

        for s in range(int(2e-3 // dt)):
            substep()

        render()
        canvas.set_background_color((0.067, 0.184, 0.255))
        canvas.circles(water, radius=radius, color=(0, 0.5, 0.5))
        window.show()


if __name__ == "__main__":
    main()
