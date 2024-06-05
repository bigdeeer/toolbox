from PySide6 import QtCore
from PySide6.QtCore import QItemSelectionModel
from PySide6.QtWidgets import QListWidget, QListWidgetItem, QWidget, QPushButton, QSizePolicy, QTextEdit
from mistune import html

from chatgpt_project.ui.dialog_ui import Ui_Dialog_item
from util.STYLE_CSS import *

EXPANDING = QSizePolicy.Policy.Expanding
MININUM = QSizePolicy.Policy.Minimum


def markdown_to_html(md):
    ht = html(md)
    ht = ht.replace('\n</code>', '</code>')
    ht = ht.replace('<pre>', CELL_CSS_BEGIN)
    ht = ht.replace('</pre>', CELL_CSS_END)
    return ht


class DialogListItemWidget(QWidget, Ui_Dialog_item):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        for button in self.findChildren(QPushButton):
            button: QPushButton
            button.setStyleSheet(BUTTON_STYLE_HIDDEN)

        self.ht_cell.setStyleSheet(VBOX_STYLE)
        self.label.setStyleSheet(LABEL_HIDDEN)
        self.dialog_cell.setStyleSheet(VBOX_STYLE)

    def render_dialog(self, dialog_obj):
        md = dialog_obj['content']
        role = dialog_obj['role']
        ht = CSS_BEGIN + markdown_to_html(md) + "</body></html>"

        if role == 'user':
            self.item_layout.setStretch(0, 1)
            self.item_layout.setStretch(2, 0)
            self.left_space.changeSize(0,0,EXPANDING,EXPANDING)
            self.right_space.changeSize(0, 0, MININUM,MININUM)
        else:
            self.item_layout.setStretch(0, 0)
            self.item_layout.setStretch(2, 1)
            self.left_space.changeSize(0,0,MININUM,MININUM)
            self.right_space.changeSize(0, 0, EXPANDING,EXPANDING)

        self.ht_cell.setHtml(ht)
        # self.ht_cell.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
        self.ht_cell.document().adjustSize()
        h = self.ht_cell.document().size().height()
        self.ht_cell.setFixedHeight(h)

        self.label.setText(role)


class DialogListItem(QListWidgetItem):

    def __init__(self, dialog_obj):
        super().__init__()
        self.widget = DialogListItemWidget()
        self.widget.render_dialog(dialog_obj)
        h = self.widget.ht_cell.height() + self.widget.label.height() + 90
        self.setSizeHint(QtCore.QSize(0, h))


class DialogList(QListWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setVerticalScrollMode(QListWidget.ScrollMode.ScrollPerPixel)
        self.setSelectionMode(QListWidget.SelectionMode.NoSelection)

    def add_item(self, dialog_obj):
        item = DialogListItem(dialog_obj)
        self.addItem(item)
        self.setItemWidget(item, item.widget)
