from PySide6.QtWidgets import QWidget, QSizePolicy

EXPAND = QSizePolicy.Policy.Expanding
FIXED = QSizePolicy.Policy.Fixed


def restrain_height(widget: QWidget):
    height = widget.minimumHeight()
    widget.setMaximumHeight(height)
    widget.setSizePolicy(EXPAND, FIXED)


def expand_height(widget: QWidget):
    widget.setMaximumHeight(8000)
    widget.setSizePolicy(EXPAND, EXPAND)
