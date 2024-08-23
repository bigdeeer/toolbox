from PySide6 import QtCore
from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QListWidget, QListWidgetItem, QWidget, QPushButton, QSizePolicy
)
from utility.style import style_sheet
from ui.dialog_ui import Ui_dialog_item
from utility.HTML_CSS import CSS_BEGIN
from func.format_func import markdown_to_html

# 定义尺寸策略的常量。
EXPANDING = QSizePolicy.Policy.Expanding
MININUM = QSizePolicy.Policy.Minimum


class DialogListItemWidget(QWidget, Ui_dialog_item):
    """
    代表对话列表中的单个 item 的小部件。
    """
    index = -1  # 消息id
    dialog_obj = {}

    def __init__(self, dialog_obj, index):
        """
        初始化小部件，设置UI并连接信号。

        :param index: 项目的唯一标识符。
        """
        super().__init__()
        self.setupUi(self)
        # 编号存入按钮属性
        self.delete_cell_btn.setProperty('index', index)
        self.dialog_obj = dialog_obj

        self.ht_cell.setReadOnly(True)
        # 连接按钮点击信号。
        self.edit_cell_btn.clicked.connect(self.switch_edit_status)
        self.pause_cell_btn.clicked.connect(self.mask_item)

        # 两种数据
        self.md_data = ""
        self.ht_data = ""

        self.render_dialog()

    def mask_item(self):
        """
        根据按钮状态显示或隐藏项目。
        """
        if self.pause_cell_btn.isChecked():
            self.pause_cell_btn.setText(" 取消屏蔽 ")
            self.dialog_obj['mask'] = True
        else:
            self.pause_cell_btn.setText(" 屏蔽 ")
            self.dialog_obj['mask'] = False

    def switch_edit_status(self):
        """ 切换文本的显示类型 """

        if self.ht_cell.isReadOnly():
            self.ht_cell.setReadOnly(False)
            self.ht_cell.setText(self.md_data)
            self.edit_cell_btn.setText(" 完成编辑 ")
        else:
            self.md_data = self.ht_cell.toPlainText()
            self.md_to_ht()
            self.ht_cell.setReadOnly(True)
            self.ht_cell.setHtml(self.ht_data)
            self.edit_cell_btn.setText(" 编辑 ")

    def md_to_ht(self):
        """ 将md转换为html """
        self.ht_data = CSS_BEGIN + markdown_to_html(self.md_data) + "</body></html>"

    def render_dialog(self):
        """
        渲染对话内容到小部件。

        :param message_obj: 包含对话内容和角色的对象。
        """
        md = self.dialog_obj['content']
        role = self.dialog_obj['role']

        self.md_data = md
        self.md_to_ht()

        # 根据角色调整布局。
        if role == 'user':
            self.item_layout.setStretch(0, 1)
            self.item_layout.setStretch(2, 0)
            self.left_space.changeSize(0, 0, EXPANDING, EXPANDING)
            self.right_space.changeSize(0, 0, MININUM, MININUM)
        else:
            self.item_layout.setStretch(0, 0)
            self.item_layout.setStretch(2, 1)
            self.left_space.changeSize(0, 0, MININUM, MININUM)
            self.right_space.changeSize(0, 0, EXPANDING, EXPANDING)

        self.ht_cell.setHtml(self.ht_data)
        self.ht_cell.document().adjustSize()
        h = self.ht_cell.document().size().height()
        self.ht_cell.setFixedHeight(h)
        self.ht_cell_frame.setFixedHeight(h + 40)

        self.role_label.setText(role)


class DialogListItem(QListWidgetItem):
    """
    代表对话列表中的单个项目。
    """
    index = -1

    def __init__(self, dialog_obj, index):
        """
        初始化列表项，渲染对话内容并设置大小提示。

        :param dialog_obj: 包含对话内容和角色的对象。
        :param index: 消息编号
        """
        super().__init__()

        # 消息编号存入属性
        self.index = index

        # 初始化widget
        self.widget = DialogListItemWidget(dialog_obj, index)

        # 尺寸
        h = self.widget.ht_cell_frame.height() + self.widget.cell_title_layout.height() + 20
        self.widget.setFixedHeight(h)
        self.setSizeHint(QtCore.QSize(0, h))


class DialogList(QListWidget):
    """
    对话列表，包含多个对话项。
    """
    current_id = 0

    def __init__(self, parent):
        """
        初始化对话列表，设置滚动模式和快捷键。

        :param parent: 父窗口。
        """
        super().__init__(parent)
        self.setVerticalScrollMode(QListWidget.ScrollMode.ScrollPerPixel)
        self.setSelectionMode(QListWidget.SelectionMode.NoSelection)
        self.setEditTriggers(QListWidget.EditTrigger.NoEditTriggers)

        self.verticalScrollBar().setSingleStep(30)

    def add_item(self, dialog_obj):
        """
        向列表中添加一个新的对话项。

        :param dialog_obj: 包含对话内容和角色的对象。
        """
        item = DialogListItem(dialog_obj, self.current_id)
        self.current_id += 1

        item.widget.delete_cell_btn.clicked.connect(self.delete_item)

        self.addItem(item)

        self.setItemWidget(item, item.widget)

        self.verticalScrollBar().setValue(self.verticalScrollBar().maximum())

    def delete_item(self):
        """
        删除具有给定ID的项目。
        """
        btn: QPushButton = self.sender()
        message_index = btn.property('index')
        for index in range(self.count()):
            if self.item(index).index == message_index:
                self.takeItem(index)
                return
