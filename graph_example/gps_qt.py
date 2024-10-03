# coding=utf8
import json
import sys
import numpy as np
import yaml
from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QMainWindow, QApplication

from gps_qt_ui import Ui_MainWindow  # 导入界面

# 默认设置和本地设置
setting = QSettings('util/setting.ini', QSettings.Format.IniFormat)


class MonitorForm(QMainWindow, Ui_MainWindow):
    polyline_pos = None  # 内存里的多边形数据

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setting_load()  # 价值配置
        self.init_signals()  # 信号
        self.polyline_load_json()  # 从文件加载多边形

    def init_signals(self):
        """信号绑定"""
        # 只和polyline有关系的方法直接绑定到内部方法
        self.edit_poly_btn.clicked.connect(self.map_widget.polyline_switch_edit_status)
        # 需要在全局操作的，绑定到self方法
        self.save_poly_btn.clicked.connect(self.polyline_save_json)
        self.restore_poly_btn.clicked.connect(self.polyline_restore)

    def setting_load(self):
        """
        加载设置
        """
        # 图片位置和图片控制点位置
        # self.map_widget.map_image.setTransform(setting.value('matrix'))
        self.map_widget.handle1.setPos(setting.value('handle_1'))
        self.map_widget.handle2.setPos(setting.value('handle_2'))
        # 窗体尺寸
        self.setFixedWidth(int(setting.value('width')))
        self.setFixedHeight(int(setting.value('height')))

    def setting_save(self):
        """
        保存设置
        """
        # 图片位置和控制点位置
        setting.setValue('matrix', self.map_widget.map_image.transform())
        setting.setValue('handle_1', self.map_widget.handle1.pos())
        setting.setValue('handle_2', self.map_widget.handle2.pos())
        # 窗体尺寸
        setting.setValue('width', self.width())
        setting.setValue('height', self.height())

    def polyline_load(self):
        """从文件加载多边形数据"""

        with open('util/polyline.yaml', 'r') as f:
            pos_list: list = yaml.load(f, Loader=yaml.FullLoader)

        # 转化为numpy数组
        pos: np.ndarray = np.array(pos_list)
        # 创建多边形
        self.map_widget.polyline_create(pos)
        # 存入内存，方便后续恢复，这里需要copy，否则将传递地址，导致内存内跟着多边形一起编辑
        self.polyline_pos = np.copy(pos)

    def polyline_save(self):
        """多边形数据存入文件"""
        # 获取多边形数据
        pos: np.ndarray = self.map_widget.polyline.pos
        # 存入yaml文件
        with open('util/polyline.yaml', 'w') as f:
            yaml.dump(pos.tolist(), f)

        # 同步存入内存
        self.polyline_pos = np.copy(pos)

    def polyline_load_json(self):
        """从文件加载多边形数据"""

        with open('util/polyline.json', 'r') as f:
            pos_list: list = json.load(f)

        # 转化为numpy数组
        pos: np.ndarray = np.array(pos_list)
        # 创建多边形
        self.map_widget.polyline_create(pos)
        # 存入内存，方便后续恢复，这里需要copy，否则将传递地址，导致内存内跟着多边形一起编辑
        self.polyline_pos = np.copy(pos)

    def polyline_save_json(self):
        """多边形数据存入文件"""
        # 获取多边形数据
        pos: np.ndarray = self.map_widget.polyline.pos
        # 存入json文件
        with open('util/polyline.json', 'w') as f:
            json.dump(pos.tolist(), f)

        # 同步存入内存
        self.polyline_pos = np.copy(pos)

    def polyline_restore(self):
        """恢复多边形数据"""
        # 从内存恢复
        self.map_widget.polyline.vertices_update(self.polyline_pos)

    def closeEvent(self, event):
        """
        关闭应用程序时保存用户设置
        :param event:
        """

        self.setting_save()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    my_monit_from = MonitorForm()
    my_monit_from.show()

    app.exec()
