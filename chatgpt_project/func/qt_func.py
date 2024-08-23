from PySide6.QtCore import QSize
from PySide6.QtGui import QImage, QPainter, QPixmap


def find_all_child(widget, include=None, exclude=None):
    # 目标集合
    target_widgets = []

    # 遍历子控件
    for child in widget.children():

        if ((include and isinstance(child, include))  # 指定了类型并且控件满足类型
                or (exclude and not isinstance(child, exclude))  # 指定了排除并且控件不是排除的类型
                or (not include and not exclude)):  # 都没有指定
            # 加入列表
            target_widgets.append(child)

        # 递归继续查找子控件
        child_widgets = find_all_child(child, include, exclude)
        # 查到的控件加入列表
        target_widgets.extend(child_widgets)
    return target_widgets


def get_colored_icon(icon_path, color, width, height):
    """给png图标上色"""

    # 载入png图片成为遮罩
    mask = QImage(icon_path)

    # 转化颜色格式
    mask = mask.convertToFormat(QImage.Format_ARGB32)

    # 创建透明填充背景
    back = QImage(QSize(width, height), QImage.Format_ARGB32)
    back.fill(color)

    # 在背景创建画笔
    painter = QPainter(back)

    # 设定画笔混合模式
    painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_DestinationIn)

    # 使用画笔讲遮罩绘制在透明背景上
    painter.drawImage(0, 0, mask)

    # 结束绘制并返回背景
    painter.end()
    return QPixmap.fromImage(back)
