# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
            dialog_item.setObjectName(u"dialog_item")
        dialog_item.resize(775, 568)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialog_item.sizePolicy().hasHeightForWidth())
        dialog_item.setSizePolicy(sizePolicy)
        self.item_layout = QHBoxLayout(dialog_item)
        self.item_layout.setSpacing(0)
        self.item_layout.setObjectName(u"item_layout")
        self.item_layout.setContentsMargins(10, 10, 10, 10)
        self.left_space = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.item_layout.addItem(self.left_space)

        self.dialog_cell = QWidget(dialog_item)
        self.dialog_cell.setObjectName(u"dialog_cell")
        sizePolicy.setHeightForWidth(self.dialog_cell.sizePolicy().hasHeightForWidth())
        self.dialog_cell.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.dialog_cell)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.cell_title_layout = QWidget(self.dialog_cell)
        self.cell_title_layout.setObjectName(u"cell_title_layout")
        self.cell_title_layout.setMinimumSize(QSize(0, 40))
        self.cell_title_layout.setMaximumSize(QSize(16777215, 40))
        self.cell_title_layout.setStyleSheet(u"border:0px")
        self.horizontalLayout = QHBoxLayout(self.cell_title_layout)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 5, 10, 5)
        self.role_label = QLabel(self.cell_title_layout)
        self.role_label.setObjectName(u"role_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.role_label.sizePolicy().hasHeightForWidth())
        self.role_label.setSizePolicy(sizePolicy1)
        self.role_label.setMinimumSize(QSize(60, 0))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.role_label.setFont(font)

        self.horizontalLayout.addWidget(self.role_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.edit_cell_btn = QPushButton(self.cell_title_layout)
        self.edit_cell_btn.setObjectName(u"edit_cell_btn")
        sizePolicy.setHeightForWidth(self.edit_cell_btn.sizePolicy().hasHeightForWidth())
        self.edit_cell_btn.setSizePolicy(sizePolicy)
        self.edit_cell_btn.setCheckable(True)

        self.horizontalLayout.addWidget(self.edit_cell_btn)

        self.pause_cell_btn = QPushButton(self.cell_title_layout)
        self.pause_cell_btn.setObjectName(u"pause_cell_btn")
        sizePolicy.setHeightForWidth(self.pause_cell_btn.sizePolicy().hasHeightForWidth())
        self.pause_cell_btn.setSizePolicy(sizePolicy)
        self.pause_cell_btn.setCheckable(True)

        self.horizontalLayout.addWidget(self.pause_cell_btn)

        self.delete_cell_btn = QPushButton(self.cell_title_layout)
        self.delete_cell_btn.setObjectName(u"delete_cell_btn")
        sizePolicy.setHeightForWidth(self.delete_cell_btn.sizePolicy().hasHeightForWidth())
        self.delete_cell_btn.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.delete_cell_btn)


        self.verticalLayout.addWidget(self.cell_title_layout)

        self.ht_cell_frame = QWidget(self.dialog_cell)
        self.ht_cell_frame.setObjectName(u"ht_cell_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ht_cell_frame.sizePolicy().hasHeightForWidth())
        self.ht_cell_frame.setSizePolicy(sizePolicy2)
        self.ht_cell_layout = QVBoxLayout(self.ht_cell_frame)
        self.ht_cell_layout.setSpacing(0)
        self.ht_cell_layout.setObjectName(u"ht_cell_layout")
        self.ht_cell_layout.setContentsMargins(20, 20, 20, 20)
        self.ht_cell = QTextEdit(self.ht_cell_frame)
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

        self.ht_cell_layout.addWidget(self.ht_cell)


        self.verticalLayout.addWidget(self.ht_cell_frame)


        self.item_layout.addWidget(self.dialog_cell)

        self.right_space = QSpacerItem(216, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.item_layout.addItem(self.right_space)

        self.item_layout.setStretch(0, 1)
        self.item_layout.setStretch(1, 2)
        self.item_layout.setStretch(2, 1)

        self.retranslateUi(dialog_item)

        QMetaObject.connectSlotsByName(dialog_item)
    # setupUi

    def retranslateUi(self, dialog_item):
        dialog_item.setWindowTitle(QCoreApplication.translate("dialog_item", u"Form", None))
        self.role_label.setText(QCoreApplication.translate("dialog_item", u"asdasdasd", None))
        self.edit_cell_btn.setText(QCoreApplication.translate("dialog_item", u" \u7f16\u8f91 ", None))
        self.pause_cell_btn.setText(QCoreApplication.translate("dialog_item", u" \u5c4f\u853d ", None))
        self.delete_cell_btn.setText(QCoreApplication.translate("dialog_item", u" \u5220\u9664 ", None))
        self.ht_cell.setHtml(QCoreApplication.translate("dialog_item", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

