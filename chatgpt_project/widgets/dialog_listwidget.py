from PySide6 import QtCore
from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QListWidget, QListWidgetItem, QWidget, QPushButton, QSizePolicy
)

from ui.dialog_ui import Ui_dialog_item
from utility.STYLE_CSS import CSS_BEGIN
from func.format_func import markdown_to_html

# 定义尺寸策略的常量。
EXPANDING = QSizePolicy.Policy.Expanding
MININUM = QSizePolicy.Policy.Minimum


class DialogListItemWidget(QWidget, Ui_dialog_item):
    """
    代表对话列表中的单个 item 的小部件。
    """
    selected = Signal(int)
    deleted = Signal(int)

    def __init__(self, id):
        """
        初始化小部件，设置UI并连接信号。

        :param id: 项目的唯一标识符。
        """
        super().__init__()
        self.setupUi(self)

        # for button in self.findChildren(QPushButton):
        #     button: QPushButton
        #     button.setProperty("style", "BUTTON_STYLE_HIDDEN")
        #
        # self.setProperty('type', 'cell')
        self.setObjectName('place')
        self.style().unpolish(self)
        self.style().polish(self)
        # self.setStyleSheet("""
        #                   background-color:rgb(50,50,50);
        #                   border:1px solid rgb(128,128,128);
        #                   border-radius:5px
        # """)

        # 设置各种UI元素的样式。
        # self.dialog_cell.setProperty("style", "DIALOG_CELL_STYLE")
        # self.label.setProperty("style", "LABEL_HIDDEN")
        # self.ht_cell.setProperty("style", "DIALOG_BOX_STYLE")

        self.ht_cell.setReadOnly(True)
        self.ht_cell.setStyleSheet("""
                          border:0px
        """)
        # 连接按钮点击信号。
        self.delete_cell_btn.clicked.connect(self.delete)

        self.id = id

        # 两种数据
        self.md_data = ""
        self.ht_data = ""

    def delete(self):
        """发射删除信号，附带项目ID。"""
        self.deleted.emit(self.id)

    def switch_edit_status(self):
        """ 切换文本的显示类型 """

        if self.ht_cell.isReadOnly():
            self.ht_cell.setReadOnly(False)
            self.ht_cell.setText(self.md_data)
        else:
            self.md_data = self.ht_cell.toPlainText()
            self.md_to_ht()
            self.ht_cell.setReadOnly(True)
            self.ht_cell.setHtml(self.ht_data)

    def md_to_ht(self):
        """ 将md转换为html """
        self.ht_data = CSS_BEGIN + markdown_to_html(self.md_data) + "</body></html>"

    def render_dialog(self, dialog_obj):
        """
        渲染对话内容到小部件。

        :param dialog_obj: 包含对话内容和角色的对象。
        """
        md = dialog_obj['content']
        role = dialog_obj['role']

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

        self.label.setText(role)


class DialogListItem(QListWidgetItem):
    """
    代表对话列表中的单个项目。
    """
    id = -1
    dialog_obj = {}

    def __init__(self, dialog_obj, id):
        """
        初始化列表项，渲染对话内容并设置大小提示。

        :param dialog_obj: 包含对话内容和角色的对象。
        :param id: 项目的唯一标识符。
        """
        super().__init__()
        self.id = id
        self.widget = DialogListItemWidget(id)
        self.widget.render_dialog(dialog_obj)
        self.dialog_obj = dialog_obj
        h = self.widget.ht_cell.height() + self.widget.label.height() + 50
        self.setSizeHint(QtCore.QSize(0, h))
        self.widget.pause_cell_btn.clicked.connect(self.mask_item)

    def mask_item(self):
        """
        根据按钮状态显示或隐藏项目。
        """
        status = self.widget.pause_cell_btn.isChecked()
        self.dialog_obj['mask'] = not status
        # if status:
        #     self.widget.dialog_cell.setProperty("style", "VBOX_STYLE")
        #     self.widget.dialog_cell.style().unpolish(self.widget.dialog_cell)
        #     self.widget.dialog_cell.style().polish(self.widget.dialog_cell)
        # else:
        #     self.widget.dialog_cell.setProperty("style", "VBOX_STYLE_MASK")
        #     self.widget.dialog_cell.style().unpolish(self.widget.dialog_cell)
        #     self.widget.dialog_cell.style().polish(self.widget.dialog_cell)


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


        # self.setStyleSheet(
        #     """
        #     border:0px;
        #     background-color:transparent;
        #     """
        # )

    def add_item(self, dialog_obj):
        """
        向列表中添加一个新的对话项。

        :param dialog_obj: 包含对话内容和角色的对象。
        """
        item = DialogListItem(dialog_obj, self.current_id)
        self.current_id += 1
        item.widget.deleted.connect(self.delete_item)
        self.addItem(item)

        self.setItemWidget(item, item.widget)
        self.verticalScrollBar().setValue(self.verticalScrollBar().maximum())

    def delete_item(self, id):
        """
        删除具有给定ID的项目。

        :param id: 要删除的项目的ID。
        """
        for index in range(self.count()):
            if self.item(index).id == id:
                self.takeItem(index)
