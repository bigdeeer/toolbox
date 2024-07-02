from PySide6 import QtCore
from PySide6.QtCore import Signal
from PySide6.QtGui import QKeySequence, QShortcut, Qt
from PySide6.QtWidgets import QListWidget, QListWidgetItem, QWidget, QPushButton, QSizePolicy, QTextEdit, QApplication
from mistune import html

from ui.dialog_ui import Ui_dialog_item
from util.STYLE_CSS import *

EXPANDING = QSizePolicy.Policy.Expanding
MININUM = QSizePolicy.Policy.Minimum


def markdown_to_html(md):
    ht = html(md)
    ht = ht.replace('\n</code>', '</code>')
    ht = ht.replace('<pre>', CELL_CSS_BEGIN)
    ht = ht.replace('</pre>', CELL_CSS_END)
    return ht


class DialogListItemWidget(QWidget, Ui_dialog_item):
    selected = Signal(int)
    deleted = Signal(int)

    def __init__(self, id):
        super().__init__()
        self.setupUi(self)

        for button in self.findChildren(QPushButton):
            button: QPushButton
            button.setStyleSheet(BUTTON_STYLE_HIDDEN)

        self.ht_cell.setStyleSheet(DIALOG_BOX_STYLE)
        self.label.setStyleSheet(LABEL_HIDDEN)
        self.dialog_cell.setStyleSheet(DIALOG_CELL_STYLE)
        self.delete_cell_btn.clicked.connect(self.delete)
        self.ht_cell.cursorPositionChanged.connect(self.select)
        self.id = id

    def delete(self):
        self.deleted.emit(self.id)

    def mousePressEvent(self, event):
        self.select()

    def select(self):
        self.selected.emit(self.id)

    def render_dialog(self, dialog_obj):
        md = dialog_obj['content']
        role = dialog_obj['role']
        ht = CSS_BEGIN + markdown_to_html(md) + "</body></html>"

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

        self.ht_cell.setHtml(ht)
        self.ht_cell.document().adjustSize()
        h = self.ht_cell.document().size().height()
        self.ht_cell.setFixedHeight(h)

        self.label.setText(role)


class DialogListItem(QListWidgetItem):
    id = -1
    dialog_obj = {}

    def __init__(self, dialog_obj, id):
        super().__init__()
        self.id = id
        self.widget = DialogListItemWidget(id)
        self.widget.render_dialog(dialog_obj)
        self.dialog_obj = dialog_obj
        h = self.widget.ht_cell.height() + self.widget.label.height() + 50
        self.setSizeHint(QtCore.QSize(0, h))
        self.widget.pause_cell_btn.clicked.connect(self.mask_item)

    def mask_item(self):
        status = self.widget.pause_cell_btn.isChecked()
        self.dialog_obj['mask'] = not status
        if status:
            self.widget.dialog_cell.setStyleSheet(VBOX_STYLE)
        else:
            self.widget.dialog_cell.setStyleSheet(VBOX_STYLE_MASK)


class DialogList(QListWidget):
    current_id = 0

    def __init__(self, parent):
        super().__init__(parent)
        self.setVerticalScrollMode(QListWidget.ScrollMode.ScrollPerPixel)
        self.setSelectionMode(QListWidget.SelectionMode.NoSelection)
        self.setEditTriggers(QListWidget.EditTrigger.NoEditTriggers)
        QShortcut(QKeySequence('Ctrl+C'), self, self.copy_text)


    def copy_text(self):
        if not self.currentItem():
            return
        textbox = self.currentItem().widget.ht_cell

        cursor = textbox.textCursor()
        selected_text = cursor.selectedText()
        selected_text = selected_text.replace(chr(8233),'\n')

        if selected_text:
            clipboard = QApplication.clipboard()
            clipboard.setText(selected_text)

    def add_item(self, dialog_obj):
        item = DialogListItem(dialog_obj, self.current_id)
        self.current_id += 1
        item.widget.deleted.connect(self.delete_item)
        item.widget.selected.connect(self.select_item)
        self.addItem(item)

        self.setItemWidget(item, item.widget)

    def select_item(self, id):
        for index in range(self.count()):
            if self.item(index).id == id:
                self.setCurrentItem(self.item(index))

    def delete_item(self, id):
        for index in range(self.count()):
            if self.item(index).id == id:
                self.takeItem(index)
