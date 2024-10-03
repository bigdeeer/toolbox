# coding=utf-8
import math
import numpy as np
import pyqtgraph as pg
import shiboken6
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtGui import QPainter, QPixmap, QVector2D, QTransform, Qt
from PySide6.QtWidgets import QApplication, QGraphicsPixmapItem, QMessageBox

from func.analyzer import dist_point_to_polygon_edges, dist_point_to_polygon_vertices


class ControlPointItem(pg.TargetItem):
    """
    多段线的控制点
    pyqtgraph的TargetItem继承类，其中多记录了顶点序号的信息
    """

    # 顶点序号
    index = 0

    def __init__(self, index=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.index = index


class PolylineItem(pg.GraphicsObject):
    """
    多段线类
    pyqtgraph的底层GraphicsObject继承类，针对曲线绘制做了性能优化
    """

    # 记录点坐标的数组，[[x1,y1],[x2,y2],[x3,y3]]的N*2二维numpy数组
    pos = None

    # 默认样式
    width = 1

    def __init__(self, style, pos=None, closed=True):
        """
        初始化
        :param: pos:控制点的位置，[[x1,y1],[x2,y2],[x3,y3]]的N*2二维numpy数组
        :param: closed:是否封闭曲线
        """
        # 基类初始化
        pg.GraphicsObject.__init__(self)
        # 初始化QPicture
        self.picture = QtGui.QPicture()

        # 读取笔刷参数并存入属性
        self.pen = style['pen']
        self.brush = style['brush']

        # 是否封闭曲线
        self.closed = closed

        # 初始化时有位置输入，则直接绘图
        if pos is not None:
            self.vertices_update(pos)

    def vertices_update(self, pos):
        """
        更新顶点位置并重绘曲线
        :param pos: 控制点的位置，[[x1,y1],[x2,y2],[x3,y3]]的N*2二维numpy数组
        """

        # 存入属性
        self.pos = pos
        # 绘制
        self.generate_polyline()

    def vertex_insert(self, point, index):
        """
        插入顶点
        :param point: QPointF类
        :param index: 插入位置
        """

        # 将点转化为numpy数组并插入
        new_point = np.array([point.x(), point.y()])
        self.pos = np.insert(self.pos, index, new_point, axis=0)
        # 绘制
        self.generate_polyline()

    def vertex_remove(self, index):
        """
        删除顶点
        :param index: 删除的顶点序号
        """

        # 从数组删除
        self.pos = np.delete(self.pos, index, axis=0)
        # 绘制
        self.generate_polyline()  # 更新数据后重新生成图片

    def generate_polyline(self):
        """
        绘制曲线
        核心代码使用pyqtgraph源码，直接对指定位置的内存进行写入
        """

        # 创建画笔和抗锯齿
        p = QtGui.QPainter(self.picture)
        p.setRenderHint(QPainter.Antialiasing)
        # 设定笔刷
        p.setPen(self.pen)
        p.setBrush(self.brush)

        # 初始化q_poly
        size = np.shape(self.pos)[0]  # 获取路径点数
        q_poly = QtGui.QPolygonF()
        q_poly.resize(size)  # 设置多边形大小

        """
        PyQtGraph封装的多边形绘制方法效率较低，为提升效率，下面的代码修改自PyQtGraph内调用Qt的核心代码
        方法位置：
        虚拟环境\Lib\site-packages\pyqtgraph\functions.py
        def ndarray_from_qpolygonf(polyline)
        以下三行不要求全部理解
        """

        vp = shiboken6.VoidPtr(q_poly.data(), size * 2 * 8, True)  # 获取多边形数据指针
        arr = np.frombuffer(vp, dtype=np.float64).reshape((-1, 2))  # 将多边形数据转换为numpy数组
        arr[:, :] = self.pos  # 将路径坐标赋值给多边形坐标,注意此处[:,:]表示切片是必须的

        path = QtGui.QPainterPath()  # 创建路径对象
        path.addPolygon(q_poly)  # 将多边形添加到路径中

        # 封闭曲线的情况下，利用QPainterPath的自带功能处理封闭
        if self.closed:
            path.closeSubpath()

        # 绘制
        p.drawPath(path)
        # 结束画笔
        p.end()

    def paint(self, p, *args):  # 内部方法，不修改
        p.drawPicture(0, 0, self.picture)  # 绘制图片

    def boundingRect(self):  # 内部方法，不修改
        return QtCore.QRectF(self.picture.boundingRect())  # 获取图片的定界框


class MapWidget(pg.PlotWidget, QtWidgets.QWidget):
    """
    继承pyqtgraph的PlotWidget类和Qt的QWidget类
    """
    # 当前显示编辑的多边形
    polyline = None
    # 当前正在编辑的控制点列表
    editing_vertices = []
    # 预览折线
    preview_edit_polyline = None

    # 当前准备插入或删除的点和边的序号
    current_seg_i = -1
    current_vertex_i = -1

    # 检测键盘功能键是否按下
    control_down = False
    shift_down = False

    def __init__(self, parent=None):
        super().__init__(parent)

        # 基础格式设定
        self.showGrid(x=False, y=False)  # 隐藏网格
        self.hideAxis('bottom')  # 隐藏横轴
        self.hideAxis('left')  # 隐藏纵轴
        self.setAspectLocked(True)  # 纵横比
        # self.setLimits(xMin=1200, xMax=8000, yMin=400, yMax=4950)  # 显示范围限定

        # 获取绘图区域和视图区域
        self.plot_item = self.getPlotItem()
        self.vb = self.plot_item.vb

        # 创建垂直和水平线
        self.v_line = self.create_infinite_line(angle=90)
        self.h_line = self.create_infinite_line(angle=0)

        width = 653961.624739
        height = 462333.2083

        # 加载地图图片
        self.map_image = QGraphicsPixmapItem(QPixmap('util/map.jpg').transformed(QtGui.QTransform().scale(1, -1)))
        scale_factor_x = width / self.map_image.pixmap().width()
        scale_factor_y = height / self.map_image.pixmap().height()
        self.map_image.setTransform(QtGui.QTransform().scale(scale_factor_x, scale_factor_y))
        self.map_image.setZValue(0)
        self.addItem(self.map_image)

        # 地图的操作手柄
        self.handle1 = self.bg_handle_create(width / 4, height / 4)
        self.handle2 = self.bg_handle_create(width / 2, height / 2)
        self.prev_point_B = pg.Point()  # 手柄开始拖动时的点位记录
        self.handle_moving = False  # 手柄是否移动的初始化值

        # 鼠标移动信号
        self.scene().sigMouseMoved.connect(self.mouse_move)
        self.scene().sigMouseClicked.connect(self.mouse_click)

    def create_infinite_line(self, angle, pos=0, label=''):
        """
        创建垂直线和水平线
        :param angle: 角度，0或者90代表水平和垂直
        :param pos: float，线的水平或垂直位置
        :param label: str，线上面的文字
        """
        # 笔刷
        pen = pg.mkPen(color=(0, 0, 0, 100))
        # 创建
        line = pg.InfiniteLine(angle=angle, movable=False, label=label, pen=pen)
        # 设定位置，标签等格式
        line.setPos(pos)
        line.label.setPosition(0.05)  # 文字显示在直线的起点附近，靠近边框位置
        line.label.setColor((0, 0, 0))
        line.setZValue(100)
        # 添加
        self.addItem(line)
        return line

    def bg_handle_create(self, x, y):
        """
        创建调整图片的控制点
        :param x: x坐标
        :param y: y坐标
        """

        # 格式
        pen = pg.mkPen(color=(0, 0, 0, 100))
        brush = pg.mkBrush(color=(255, 0, 0, 75))

        # 创建移动手柄点
        handle = pg.TargetItem(pen=pen, brush=brush)
        self.addItem(handle)

        # 设定位置
        handle.setZValue(100)
        handle.setPos(x, y)

        # 信号绑定
        handle.sigPositionChanged.connect(self.bg_handle_move)  # 拖拽开始
        handle.sigPositionChangeFinished.connect(self.bg_handle_stop)  # 拖拽结束

        return handle

    def bg_handle_move(self):
        """
        控制图片的手柄移动时
        """

        # 如果没有按下Ctrl键，退出
        if not self.control_down:
            return

        # 根据当前正在移动的handle是哪个，决定h0和h1
        if self.sender() == self.handle1:
            h0 = self.handle2
            h1 = self.handle1
        else:
            h0 = self.handle1
            h1 = self.handle2

        # 如果当前状态是手柄已经在移动,
        if self.handle_moving:

            # 记录固定手柄的位置到a向量
            pos = h0.pos()
            v_a = QVector2D(pos.x(), pos.y())
            # 记录上一个移动手柄的位置到b向量
            pos = self.prev_point_B
            v_b = QVector2D(pos.x(), pos.y())
            # 记录当前移动手柄的位置到c向量
            pos = h1.pos()
            v_c = QVector2D(pos.x(), pos.y())
            # 用向量差计算ab和ac向量
            v_ab = v_b - v_a
            v_ac = v_c - v_a

            # 计算从ab到ac的缩放量
            scale = v_ac.length() / v_ab.length()
            # 计算从ab到ac的旋转角度
            theta = math.atan2(v_ac.y(), v_ac.x()) - math.atan2(v_ab.y(), v_ab.x())

            # 计算ab到ac的变换矩阵
            t1 = QTransform().translate(-v_a.x(), -v_a.y())
            t2 = QTransform().fromScale(scale, scale)
            t3 = QTransform().rotateRadians(theta)
            t4 = QTransform().translate(v_a.x(), v_a.y())

            # 将ab到ac的变换矩阵附加到原始的图片变形矩阵上
            matrix = self.prev_matrix * t1 * t2 * t3 * t4
            # 使用计算完毕的矩阵变换图片
            self.map_image.setTransform(matrix)

        # 如果当前状态手柄不在移动,说明是刚刚开始移动
        else:
            print('handle release')
            # 将当前手柄位置录入”上一个移动手柄的位置“
            self.prev_point_B = h1.pos()
            # 设定手柄移动
            self.handle_moving = True
            # 记录当前图片的变换矩阵
            self.prev_matrix = self.map_image.transform()

    def bg_handle_stop(self):
        """
        手柄停止移动
        """
        # 重置手柄移动状态
        self.handle_moving = False

    def mouse_move(self, pos):
        """
        鼠标移动事件
        :param pos: 鼠标位置,QPointF格式
        :return:
        """
        # 获取坐标
        mouse_point = self.vb.mapSceneToView(pos)  # 鼠标坐标换算为视图坐标
        x = mouse_point.x()  # 获取x坐标
        y = mouse_point.y()  # 获取x坐标

        # 横竖线位置更新
        self.v_line.setPos(x)
        self.v_line.label.setText(str(round(x, 2)))
        self.h_line.setPos(y)
        self.h_line.label.setText(str(round(y, 2)))

        # shift按下时
        if self.shift_down:
            # 获取当前多边形数据
            pos = self.polyline.pos
            # 求出离开鼠标最近的边缘序号
            edges_min_index = dist_point_to_polygon_edges((x, y), pos)
            # 存入属性
            self.current_seg_i = edges_min_index

            # 求出新顶点前后相邻的顶点
            next_index = (edges_min_index + 1) % pos.shape[0]
            prev_vertice = self.polyline.pos[edges_min_index]
            next_vertice = self.polyline.pos[next_index]
            # 创建预览用的折线数据，三个点
            edit_pos = [prev_vertice, [x, y], next_vertice]
            # 绘制临时预览用折线
            self.preview_edit_polyline.vertices_update(edit_pos)

            self.update()

        # ctrl按下时
        if self.control_down:
            # 获取当前多边形数据
            pos = self.polyline.pos
            # 求出离开鼠标最近的顶点序号
            vertices_min_index = dist_point_to_polygon_vertices((x, y), pos)
            # 存入属性
            self.current_vertex_i = vertices_min_index

            # 求出删除完毕后相邻的顶点
            prev_index = vertices_min_index - 1
            next_index = (vertices_min_index + 1) % pos.shape[0]
            prev_vertice = self.polyline.pos[prev_index]
            next_vertice = self.polyline.pos[next_index]
            # 创建预览用的折线数据，两个点
            edit_pos = [prev_vertice, next_vertice]
            # 绘制临时预览用折线
            self.preview_edit_polyline.vertices_update(edit_pos)

            self.update()

    def mouse_click(self, ev):
        """
        鼠标点击事件
        :param ev: 注意这里获取位置必须再调用.pos
        :return:
        """
        # 获取当前鼠标位置，做好坐标转化，格式QPointF
        mouse_point = self.vb.mapSceneToView(ev.pos())

        # 当前shift按下
        if self.shift_down:
            # 插入控制点
            self.polyline.vertex_insert(mouse_point, self.current_seg_i + 1)
            # 显示新的控制点并刷新绘图
            self.polyline_show_vertices()
            self.update()

        # 当前ctrl按下
        if self.control_down:
            # 去除控制点
            if self.polyline.pos.shape[0] < 4:
                QMessageBox.information(self, '？', '？')
                return
            self.polyline.vertex_remove(self.current_vertex_i)
            # 显示新的控制点并刷新绘图
            self.polyline_show_vertices()
            self.update()

    def keyPressEvent(self, ev):
        """
        键盘按下事件，检测shift和ctrl按下情况
        :param ev:
        :return:
        """
        if ev.modifiers() == QtCore.Qt.KeyboardModifier.ControlModifier and self.editing_vertices:
            self.control_down = True
            self.preview_edit_polyline.show()  # 显示预览折线
        if ev.modifiers() == QtCore.Qt.KeyboardModifier.ShiftModifier and self.editing_vertices:
            self.shift_down = True
            self.preview_edit_polyline.show()  # 显示预览折线

    def keyReleaseEvent(self, ev):
        """
        键盘释放事件，检测shift和ctrl释放情况
        :param ev:
        :return:
        """
        if QApplication.keyboardModifiers() == QtCore.Qt.KeyboardModifier.ControlModifier:
            self.control_down = False
            self.preview_edit_polyline.hide()  # 隐藏预览折线
        if QApplication.keyboardModifiers() == QtCore.Qt.KeyboardModifier.ShiftModifier:
            self.shift_down = False
            self.preview_edit_polyline.hide()  # 隐藏预览折线

    def polyline_create(self, pos):

        # 当前路径对象
        style = {
            'pen': pg.mkPen(color=(0, 0, 0, 192), width=1),
            'brush': pg.mkBrush(color=(255, 0, 0, 128))
        }  # 格式
        self.polyline = PolylineItem(style, pos=pos)
        self.polyline.setZValue(100)
        self.addItem(self.polyline)

        # 临时预览路径对象
        style = {
            'pen': pg.mkPen(color=(0, 0, 0, 255), width=2),
            'brush': Qt.BrushStyle.NoBrush
        }  # 格式
        self.preview_edit_polyline = PolylineItem(style, closed=False)
        self.preview_edit_polyline.setZValue(100)
        self.addItem(self.preview_edit_polyline)
        self.preview_edit_polyline.hide()  # 默认隐藏

        self.update()  # 重绘

    def polyline_switch_edit_status(self):
        """
        切换控制点打开和关闭的状态，从主程序Ctrl+E直接通信
        """
        # 当前存在打开的控制点
        if self.editing_vertices:
            # 从地图控件中隐藏所有控制点
            self.polyline_hide_vertices()
        # 当前不存在打开的控制点
        else:
            # 显示所有控制点
            self.polyline_show_vertices()

    def polyline_show_vertices(self):
        """
        打开所有控制点
        """
        # 先关闭所有控制点
        self.polyline_hide_vertices()

        pen = pg.mkPen(color=(0, 0, 0, 100))
        brush = pg.mkBrush(color=(0, 255, 0, 75))

        # 渲染所有控制点
        for i, pos in enumerate(self.polyline.pos):
            handle = ControlPointItem(pos=pos, pen=pen, brush=brush, index=i)
            handle.setLabel(str(i))
            handle.sigPositionChanged.connect(self.polyline_update_vertices)
            self.editing_vertices.append(handle)
            self.addItem(handle)

        self.update()  # 重绘
        self.setFocus()  # 指定焦点，否则无法响应键盘

    def polyline_hide_vertices(self):
        """
        关闭所有控制点
        """
        # 从列表中读取并移出地图控件
        for handle in self.editing_vertices:
            self.removeItem(handle)
        # 清空列表
        self.editing_vertices.clear()
        self.update()  # 重绘

    def polyline_update_vertices(self):
        """
        编辑控制点
        :return:
        """

        # 获取发送信号方
        handle: ControlPointItem = self.sender()
        # 获取操作的控制点的坐标
        i = handle.index
        # 获取当前任务多边形的位置数组
        pos = self.polyline.pos
        # 编辑数组内的元素
        pos[i] = handle.pos()
        # 更新多边形形状
        self.polyline.vertices_update(pos)
        # 更新图形
        self.update()  # 重绘
