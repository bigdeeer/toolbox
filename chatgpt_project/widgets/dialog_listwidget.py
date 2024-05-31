from PySide6 import QtCore
from PySide6.QtWidgets import QListWidget, QListWidgetItem, QWidget

from chatgpt_project.ui.dialog_ui import Ui_Dialog_item


class DialogListItemWidget(QWidget,Ui_Dialog_item):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class DialogListItem(QListWidgetItem):

    def __init__(self, ht):
        super().__init__()
        self.widget = DialogListItemWidget()
        self.widget.ht_cell.setHtml(ht)
        self.setSizeHint(QtCore.QSize(0, 200))


class DialogList(QListWidget):
    def __init__(self, parent):
        super().__init__(parent)

    def add_item(self, ht):
        item = DialogListItem(ht)
        self.addItem(item)
        self.setItemWidget(item, item.widget)

