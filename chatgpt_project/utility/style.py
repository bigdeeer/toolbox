# coding:utf-8
import os
from string import Template
import yaml
from PySide6.QtGui import QColor


class QssTemplate(Template):
    """
    QSS模板类，用于简化QSS样式表的字符串替换
    """

    # 设置模板字符串的分隔符为'--'
    delimiter = '--'


class ColorTemplate:
    # 颜色字典
    colors = {}

    def __init__(self):
        # 读取颜色字典
        file_name = "color.yaml"
        file_path = os.path.join(os.path.dirname(__file__), file_name)
        with open(file_path, 'r', encoding='utf-8') as f:
            self.colors = yaml.safe_load(f)

    def get_color(self, name, _type):
        """获取颜色"""
        color_obj = self.colors[name]

        # 已经存在于缓存时直接读取
        if _type in color_obj:
            return color_obj[_type]

        # 不存在时构筑
        else:
            [r, g, b] = color_obj['color']

            if _type == 'QSS':
                return f"rgb({r},{g},{b})"
            elif _type == 'QT':
                return QColor(r, g, b)


def replace_color(qss_string):
    """
    替换字符串内的颜色
    """
    # 使用Qt Template功能
    template = QssTemplate(qss_string)

    # 创建一个映射字典
    mappings = {}
    for name, color_obj in color_template.colors.items():
        mappings[name] = color_template.get_color(name, 'QSS')

    # 使用映射字典将颜色变量替换为实际颜色值
    return template.substitute(mappings)


class StyleSheet:
    style = {}

    def __init__(self):
        """ 加载QSS样式表 """

        # 本文件目录
        self.dir = os.path.dirname(os.path.abspath(__file__))
        # 找到本目录下所有QSS开头的文件夹
        for dir_name in os.listdir(self.dir):
            if dir_name.startswith("QSS"):

                # 加载QSS文件夹内的qss
                self.load_qss(dir_name)

    def load_qss(self, qss_name):
        """加载某个类系的QSS"""

        style = ""

        # 遍历所有QSS文件夹内的qss文件
        qss_dir = os.path.join(self.dir, qss_name)
        for qss_file_name in os.listdir(qss_dir):
            # 拼接qss文件路径
            qss_file_path = os.path.join(qss_dir, qss_file_name)
            # 读取
            with open(qss_file_path, 'r', encoding='utf-8') as f:
                current_style = f.read()
                # 拼接到一起
                style += current_style

        # 替换颜色并存入字典
        self.style[qss_name] = replace_color(style)


# 实例化
color_template = ColorTemplate()
style_sheet = StyleSheet()
