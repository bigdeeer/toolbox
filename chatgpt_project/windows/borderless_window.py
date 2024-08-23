# coding=utf8
import copy
import os

from PySide6.QtGui import QPixmap, QColor, QIcon, QImage, QPainter

from func.qt_func import find_all_child, get_colored_icon
from utility.setting import setting
from PySide6.QtCore import QPointF, QRect, QPoint, Qt, QSize
from PySide6.QtWidgets import (QPushButton, QMainWindow, QWidget)

from ui.chatgpt_ui import Ui_MainWindow
from utility.style import style_sheet, color_template

# region 全局变量
# 鼠标指针字典
WINDOW_CURSOR_DICT = {
    0: Qt.CursorShape.ArrowCursor,
    1: Qt.CursorShape.SizeVerCursor,
    4: Qt.CursorShape.SizeHorCursor,
    3: Qt.CursorShape.SizeBDiagCursor,
    5: Qt.CursorShape.SizeFDiagCursor
}

# 鼠标边缘检测距离
BORDER_DETECT_GAP = 10

icon_dir = 'icon/'  # 获取图标文件夹路径
ICON_DICT = {"pin_btn": [{'state': QIcon.State.On, 'file': f"{icon_dir}/pin.png"},
                         {'state': QIcon.State.Off, 'file': f"{icon_dir}/pinoff.png"}],
             "min_btn": [{'state': QIcon.State.Off, 'file': f"{icon_dir}/min.png"}],
             "max_btn": [{'state': QIcon.State.On, 'file': f"{icon_dir}/mid.png"},
                         {'state': QIcon.State.Off, 'file': f"{icon_dir}/max.png"}],
             "exit_btn": [{'state': QIcon.State.Off, 'file': f"{icon_dir}/close.png"}],
             "system_size_btn": [{'state': QIcon.State.On, 'file': f"{icon_dir}/down.png"},
                                 {'state': QIcon.State.Off, 'file': f"{icon_dir}/up.png"}],
             "input_size_btn": [{'state': QIcon.State.On, 'file': f"{icon_dir}/down.png"},
                                {'state': QIcon.State.Off, 'file': f"{icon_dir}/up.png"}],
             "send_btn": [{'state': QIcon.State.Off, 'file': f"{icon_dir}/send.png"}],
             "clear_btn": [{'state': QIcon.State.Off, 'file': f"{icon_dir}/clear.png"}]
             }


# 加载配置文件


class BorderLessWindow(QMainWindow, Ui_MainWindow):
    """程序的无边框
    该类继承自QMainWindow类，并实现了Ui_MainWindow类中的所有方法。
    它是一个无边框的窗口，可以实现窗口的拖动、缩放等功能。

    - 该类用于配置程序的基本设置和不常变动的设置，包括窗口的标题、图标、布局等。
    - 同时，该类还提供了一些常用的方法和属性，例如鼠标状态、窗口最大化之前的geometry等。
    """

    # 记录最大化之前窗体的geometry用于最大化以后的恢复
    window_max_last_geo = None
    # 鼠标状态
    mouse_state = {

        'flag_x': 0,  # 标识窗体在左右边框的情况，-4=左边缘，4=右边缘，0=不在边缘
        'flag_y': 0,  # 标识窗体在上下边框的情况，-1=上边缘，1=下边缘，0=不在边缘
        'current_local_pos': QPointF(0, 0),  # 鼠标当前位置
        'is_left_down': False,  # 左键是否按下
        'on_frame': False,  # 鼠标是否在边框
        'on_title': False,  # 鼠标是否在标题栏
        'drag_begin': False,  # 是否已经开始拖动
        'last_geo': QRect(),  # 鼠标开始操作的瞬间窗体的geometry
        'last_global_pos': QPointF(0, 0)  # 鼠标开始操作的瞬间记录的指针位置
    }

    setting_params = {}

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 初始化所有控件
        self.load_setting()  # 读取Qt设置文件
        self.load_style()  # 其他控件的样式初始化
        self.init_signal()  # 信号绑定

    def load_setting(self):
        """
        读取Qt设置文件
        """
        params = copy.deepcopy(setting.items)
        self.setting_params = params

        geo = self.geometry()
        geo.setLeft(params['left'])
        geo.setTop(params['top'])
        geo.setWidth(params['width'])
        geo.setHeight(params['height'])
        self.setGeometry(geo)

    def init_signal(self):
        """
        绑定信号和开启鼠标捕捉
        """
        self.exit_btn.clicked.connect(self.window_close)
        self.min_btn.clicked.connect(self.window_min)
        self.max_btn.clicked.connect(self.window_max)
        self.pin_btn.clicked.connect(self.window_pin)

        self.setMouseTracking(True)
        non_button_widgets = find_all_child(self, exclude=QPushButton)
        for widget in non_button_widgets:
            try:
                widget.setMouseTracking(True)
            except:
                pass

    def load_style(self):
        """ 加载样式 """
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # 无边框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 倒圆角需要

        # 样式
        self.setStyleSheet(style_sheet.style['QSS-main'])
        # 图标
        self.load_icon(color_template.get_color('LIGHT', 'QT'))

    def load_icon(self, color):
        """ 更新图标颜色 """

        # 找到所有按钮
        for btn in self.findChildren(QPushButton):
            btn: QPushButton

            # 找到已经存在于字典的按钮
            name = btn.objectName()
            if name in ICON_DICT:

                # 新建图标
                icon = QIcon()
                # 遍历不同状态
                for item in ICON_DICT[name]:
                    # 找到图片文件
                    icon_path = item['file']
                    # 给图标上色
                    pixmap = get_colored_icon(icon_path, color, 30, 30)
                    # 加载到icon中
                    icon.addPixmap(pixmap, QIcon.Normal, item['state'])

                # 设定图标
                btn.setIcon(icon)

        # 标题栏图标
        icon_path = icon_dir + "logo_trans.png"
        # 给图标上色
        pixmap = get_colored_icon(icon_path, color, 40, 30)
        # 设定图标
        self.logo_label.setPixmap(pixmap)

    def mouseMoveEvent(self, event):
        """
        鼠标移动事件
        注意需要在窗体开启mouseTracking才能正常使用这个函数
        """
        # 处理移动的原生事件
        super().mouseMoveEvent(event)

        # 获取鼠标当前世界坐标
        x = event.globalPosition().x()
        y = event.globalPosition().y()
        # 记录到状态字典
        self.mouse_state['current_local_pos'] = event.position()

        # 根据鼠标位置更新指针形状
        self.mouse_update_cursor()

        # 如果左键并未按下，退出
        if not self.mouse_state['is_left_down']:
            return

        # 鼠标在边框或标题栏
        if self.mouse_state['on_frame'] or self.mouse_state['on_title']:

            # 鼠标还没开始拖动
            # todo 有bug 拖到能显示的最小位置时 在继续页面位置会改变
            if not self.mouse_state['drag_begin']:
                # 鼠标标记为开始拖动
                self.mouse_state['drag_begin'] = True
                # 记录鼠标开始拖动时的窗体geometry以及鼠标的位置
                self.mouse_state['last_geo'] = self.geometry()
                self.mouse_state['last_global_pos'] = event.globalPosition()
            # 鼠标已经开始拖动
            else:
                # 计算鼠标当前位置和开始拖动时的位置差
                delta_x = x - self.mouse_state['last_global_pos'].x()
                delta_y = y - self.mouse_state['last_global_pos'].y()

                # 处理在窗体边缘时的geometry更新
                if self.mouse_state['on_frame']:

                    # 拖动左侧：修改左侧，右侧不变，窗体宽度会自动变化
                    if self.mouse_state['flag_x'] == -4:
                        geo = self.geometry()
                        last_left = self.mouse_state['last_geo'].left()
                        current_left = last_left + delta_x
                        geo.setLeft(current_left)
                        self.setGeometry(geo)

                    # 拖动右侧：修改宽度，左侧不变
                    if self.mouse_state['flag_x'] == 4:
                        geo = self.geometry()
                        last_width = self.mouse_state['last_geo'].width()
                        width = last_width + delta_x
                        geo.setWidth(width)
                        self.setGeometry(geo)

                    # 拖动顶部：修改顶部，底部不变，窗体高度自动变化
                    if self.mouse_state['flag_y'] == -1:
                        geo = self.geometry()
                        last_top = self.mouse_state['last_geo'].top()
                        current_top = last_top + delta_y
                        geo.setTop(current_top)
                        self.setGeometry(geo)

                    # 拖动底部：修改高度，顶部不变
                    if self.mouse_state['flag_y'] == 1:
                        geo = self.geometry()
                        last_height = self.mouse_state['last_geo'].height()
                        height = last_height + delta_y
                        geo.setHeight(height)
                        self.setGeometry(geo)

                # 处理在标题栏时的geometry更新，直接根据位置差移动左上角
                if self.mouse_state['on_title']:
                    geo = self.geometry()
                    last_corner = self.mouse_state['last_geo'].topLeft()
                    current_corner = last_corner + QPoint(delta_x, delta_y)
                    geo.moveTopLeft(current_corner)
                    self.setGeometry(geo)

    def mousePressEvent(self, event):
        """
        鼠标按下，左键按下时更新到状态
        :param event: 鼠标事件
        :return:
        """
        if event.button() == Qt.MouseButton.LeftButton:
            self.mouse_state['is_left_down']: bool = True

    def mouseReleaseEvent(self, event):
        """
        鼠标释放，左键释放时更新状态，并恢复drag_begin
        :param event: 鼠标事件
        :return:
        """
        if event.button() == Qt.MouseButton.LeftButton:
            self.mouse_state['is_left_down'] = False
            self.mouse_state['drag_begin'] = False

    def mouse_update_cursor(self):
        """
        鼠标指针更新
        :return:
        """

        # 左键已经按住时，指针不更新
        if self.mouse_state['is_left_down']:
            return

        # 从状态字典获取当前鼠标位置
        x, y = self.mouse_state['current_local_pos'].x(), self.mouse_state['current_local_pos'].y()
        # 窗体尺寸
        w, h = self.width(), self.height()

        # 检测鼠标在左右边框的状态
        if x < BORDER_DETECT_GAP:
            self.mouse_state['flag_x'] = -4
        elif x > w - BORDER_DETECT_GAP:
            self.mouse_state['flag_x'] = 4
        else:
            self.mouse_state['flag_x'] = 0
        #  检测鼠标在上下边框的状态
        if y < BORDER_DETECT_GAP:
            self.mouse_state['flag_y'] = -1
        elif y > h - BORDER_DETECT_GAP:
            self.mouse_state['flag_y'] = 1
        else:
            self.mouse_state['flag_y'] = 0

        # 将两个方向的flag相加后取绝对值，借助字典获取到样式
        cursor_flag = abs(self.mouse_state['flag_x'] + self.mouse_state['flag_y'])
        self.setCursor(WINDOW_CURSOR_DICT[cursor_flag])

        # 更新鼠标状态：是否在边框
        self.mouse_state['on_frame'] = (cursor_flag != 0)

        # 更新鼠标状态：是否在标题栏
        if self.titlebar_layout.height() > y > BORDER_DETECT_GAP and x < self.min_btn.geometry().left():
            self.mouse_state['on_title'] = True
            self.setCursor(Qt.CursorShape.SizeAllCursor)
        else:
            self.mouse_state['on_title'] = False

    def mouseDoubleClickEvent(self, event):
        """
        重写鼠标双击事件，检测鼠标是否在标题栏，如果是则最大化或还原窗口。
        :param event:
        :return:
        """
        if self.mouse_state['on_title']:
            self.max_btn.click()

    def save_setting(self):
        """
        保存设置到Qt设置文件。
        """
        # 先保存几何信息
        self.setting_params['left'] = self.geometry().left()
        self.setting_params['top'] = self.geometry().top()
        self.setting_params['width'] = self.geometry().width()
        self.setting_params['height'] = self.geometry().height()
        setting.save(self.setting_params)

    def window_min(self):
        """
        槽函数：最小化窗体界面。
        :return:
        """
        self.showMinimized()

    def window_max(self):
        """
        槽函数：最小化和恢复窗体界面
        :return:
        """
        btn = self.max_btn
        if btn.isChecked():
            self.window_max_last_geo = self.geometry()
            self.setGeometry(self.screen().availableGeometry())
        else:
            self.setGeometry(self.window_max_last_geo)

    def window_pin(self):
        """ 置顶 """

        btn = self.pin_btn
        if btn.isChecked():
            self.setWindowFlags(self.windowFlags() |
                                Qt.WindowType.WindowStaysOnTopHint)
        else:
            self.setWindowFlags(self.windowFlags() &
                                ~Qt.WindowType.WindowStaysOnTopHint)
        self.show()

    def window_close(self):
        """
        槽函数：点击界面右上角关闭按钮后，关闭界面
        :return:
        """
        self.close()

