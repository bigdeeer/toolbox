import numpy as np


def dist_point_to_polygon_vertices(p_tuple, pos):
    """
    计算点到多边形顶点的最小距离
    :param p_tuple: (x,y)元组
    :param pos: [[x1,y1],[x2,y2],[x3,y3]]的N*2二维numpy数组
    :return vertices_min_index: 最近的顶点编号
    :return vertices_min_dist: 到最近的顶点距离
    """

    p = np.array(p_tuple)

    # 求坐标差值并用norm计算向量长度
    vertices_dist_arr = np.linalg.norm(p - pos, axis=1)
    # 最小值的序号和最小值
    vertices_min_index = np.argmin(vertices_dist_arr)

    return vertices_min_index


def dist_point_to_polygon_edges(p_tuple, pos):
    """
    点到多边形边的最小距离
    :param p_tuple: (x,y)元组
    :param pos: [[x1,y1],[x2,y2],[x3,y3]]的N*2二维numpy数组
    :return edges_min_index: 最近的边编号，找不到边则返回-1
    :return edges_min_dist: 到最近的边距离，找不到边则返回无穷大
    """

    x, y = p_tuple

    # xy的差值
    dx = np.diff(pos[:, 0], append=pos[0, 0])
    dy = np.diff(pos[:, 1], append=pos[0, 1])

    # 求出参数t和遮罩
    t = ((x - pos[:, 0]) * dx + (y - pos[:, 1]) * dy) / (dx ** 2 + dy ** 2)
    mask = (t >= 0) & (t <= 1)

    # 遮罩存在至少一个True
    if np.sum(mask) > 0:
        # 最近点
        closest_x = pos[:, 0] + t * dx
        closest_y = pos[:, 1] + t * dy
        # 求出距离
        edges_dist_arr = np.sqrt((x - closest_x) ** 2 + (y - closest_y) ** 2)
        # 这里用where函数将mask=False的元素给定无穷大，确保argmin计算正确
        edges_dist_arr = np.where(mask, edges_dist_arr, np.inf)
        # 最小值的位置和数值
        edges_min_index = np.argmin(edges_dist_arr)

        return edges_min_index

    # 遮罩全部为False，所有点的t值都在0-1范围以外，返回无穷大作为最小值
    else:
        return -1
