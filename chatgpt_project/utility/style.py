# coding:utf-8
import os
from enum import Enum
from string import Template



class ThemeDefault(Enum):
    """
    定义一个表示深色主题的枚举类，包含各种界面元素的颜色属性。
    """

    BORDER_COLOR = 'rgb(96, 96, 96)'  # 深灰色。
    DEFAULT_BG = 'rgb(54, 57, 63)'  # 深灰色。
    CHECKED_BG = 'rgb(78, 81, 87)'  # 深灰色。
    HOVER_BG = 'rgb(130, 153, 206)'  # 浅蓝色。
    PRESSED_BG = 'rgb(171, 105, 135)'  # 深紫色。
    MASK_CELL = 'rgb(150, 128, 124)'  # 深棕色。
    CODE_COLOR = 'rgb(192, 192, 192)'  # 浅灰色。
    CODE_BG = 'rgb(41, 44, 46)'  # 深灰色。
    PRE_COLOR = 'rgb(238, 157, 56)'  # 橙色。
    PRE_BG = 'rgb(73, 68, 57)'  # 深棕色。


class QssTemplate(Template):
    """
    QSS模板类，用于简化QSS样式表的字符串替换
    """

    # 设置模板字符串的分隔符为'--'
    delimiter = '--'


def apply_theme_color(qss: str):
    """
    将主题颜色应用到QSS样式字符串中。

    :param qss: 原始QSS样式字符串
    :return: 替换颜色后的QSS样式字符串
    """
    template = QssTemplate(qss)

    # 创建一个字典，将ThemeDefault枚举中的成员名映射到其对应的颜色值
    mappings = {}
    for name, member in ThemeDefault.__members__.items():
        mappings[name] = member.value

    # 使用字符串模板将颜色变量替换为实际颜色值
    qss = template.substitute(mappings)

    return qss


def get_stylesheet(file: str):
    """
    从指定的QSS文件中读取样式表内容。

    :param file: QSS文件名
    :return: QSS文件的内容字符串
    """
    if not file:
        return

    with open(file, 'r', encoding='utf-8') as f:
        qss = f.read()

    # print(f"debug: get_stylesheet 获取qss样式文件成功")
    return qss


def get_qss_path():
    """
    根据控件名获取其对应的QSS文件的路径。

    :param widget_name: 控件名
    :return: QSS文件的路径
    """

    # 定义的QSS文件列表，用于检查传入的控件名是否有效

    file_dir = os.path.dirname(os.path.abspath(__file__))
    qss_dir = os.path.join(file_dir, "QSS")
    qss_file_paths = [os.path.join(qss_dir, f) for f in os.listdir(qss_dir)]
    return qss_file_paths


def load_stylesheet():
    """ 加载QSS样式表 """

    styles = ''

    qss_files = get_qss_path()
    for f in qss_files:
        qss_str = get_stylesheet(f)
        qss_str = apply_theme_color(qss_str)
        styles += qss_str

    # 如果样式表内容为空，则打印错误信息并返回
    if not styles:
        print(f"debug: 样式表为空, 样式设置失败。")
        return ""
    return styles
