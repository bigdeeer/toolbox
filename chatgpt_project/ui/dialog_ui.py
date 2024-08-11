# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_dialog_item(object):
    def setupUi(self, dialog_item):
        if not dialog_item.objectName():
            dialog_item.setObjectName(u"dialog_obj")
        dialog_item.resize(895, 653)
        self.item_layout = QHBoxLayout(dialog_item)
        self.item_layout.setSpacing(0)
        self.item_layout.setObjectName(u"item_layout")
        self.item_layout.setContentsMargins(10, 10, 10, 10)
        self.left_space = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.item_layout.addItem(self.left_space)

        self.dialog_cell = QWidget(dialog_item)
        self.dialog_cell.setObjectName(u"dialog_cell")
        self.verticalLayout = QVBoxLayout(self.dialog_cell)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 5, 10, 5)
        self.title = QWidget(self.dialog_cell)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(0, 30))
        self.title.setMaximumSize(QSize(16777215, 30))
        self.title.setStyleSheet(u"border:0px")
        self.horizontalLayout = QHBoxLayout(self.title)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.title)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(60, 0))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.edit_cell_btn = QPushButton(self.title)
        self.edit_cell_btn.setObjectName(u"edit_cell_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.edit_cell_btn.sizePolicy().hasHeightForWidth())
        self.edit_cell_btn.setSizePolicy(sizePolicy1)
        self.edit_cell_btn.setMinimumSize(QSize(0, 30))
        self.edit_cell_btn.setMaximumSize(QSize(100, 30))
        self.edit_cell_btn.setCheckable(True)

        self.horizontalLayout.addWidget(self.edit_cell_btn)

        self.pause_cell_btn = QPushButton(self.title)
        self.pause_cell_btn.setObjectName(u"pause_cell_btn")
        sizePolicy1.setHeightForWidth(self.pause_cell_btn.sizePolicy().hasHeightForWidth())
        self.pause_cell_btn.setSizePolicy(sizePolicy1)
        self.pause_cell_btn.setMinimumSize(QSize(30, 30))
        self.pause_cell_btn.setMaximumSize(QSize(100, 30))
        self.pause_cell_btn.setCheckable(True)
        self.pause_cell_btn.setChecked(True)

        self.horizontalLayout.addWidget(self.pause_cell_btn)

        self.delete_cell_btn = QPushButton(self.title)
        self.delete_cell_btn.setObjectName(u"delete_cell_btn")
        sizePolicy1.setHeightForWidth(self.delete_cell_btn.sizePolicy().hasHeightForWidth())
        self.delete_cell_btn.setSizePolicy(sizePolicy1)
        self.delete_cell_btn.setMinimumSize(QSize(30, 30))
        self.delete_cell_btn.setMaximumSize(QSize(100, 30))

        self.horizontalLayout.addWidget(self.delete_cell_btn)


        self.verticalLayout.addWidget(self.title)

        self.ht_cell = QTextEdit(self.dialog_cell)
        self.ht_cell.setObjectName(u"ht_cell")
        font1 = QFont()
        font1.setPointSize(12)
        self.ht_cell.setFont(font1)
        self.ht_cell.setFocusPolicy(Qt.StrongFocus)
        self.ht_cell.setStyleSheet(u"")
        self.ht_cell.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ht_cell.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ht_cell.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.ht_cell.setReadOnly(False)

        self.verticalLayout.addWidget(self.ht_cell)


        self.item_layout.addWidget(self.dialog_cell)

        self.right_space = QSpacerItem(216, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.item_layout.addItem(self.right_space)

        self.item_layout.setStretch(0, 1)
        self.item_layout.setStretch(1, 2)
        self.item_layout.setStretch(2, 1)

        self.retranslateUi(dialog_item)

        QMetaObject.connectSlotsByName(dialog_item)
    # setupUi

    def retranslateUi(self, dialog_item):
        dialog_item.setWindowTitle(QCoreApplication.translate("dialog_obj", u"Form", None))
        self.label.setText(QCoreApplication.translate("dialog_obj", u"asdasdasd", None))
        self.edit_cell_btn.setText(QCoreApplication.translate("dialog_obj", u" Markdown ", None))
        self.pause_cell_btn.setText(QCoreApplication.translate("dialog_obj", u" Active ", None))
        self.delete_cell_btn.setText(QCoreApplication.translate("dialog_obj", u" Delete ", None))
        self.ht_cell.setHtml(QCoreApplication.translate("dialog_obj", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

