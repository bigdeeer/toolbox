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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Dialog_item(object):
    def setupUi(self, Dialog_item):
        if not Dialog_item.objectName():
            Dialog_item.setObjectName(u"Dialog_item")
        Dialog_item.resize(589, 332)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog_item.sizePolicy().hasHeightForWidth())
        Dialog_item.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(Dialog_item)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog_item)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_3 = QPushButton(Dialog_item)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(Dialog_item)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(Dialog_item)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.ht_cell = QTextEdit(Dialog_item)
        self.ht_cell.setObjectName(u"ht_cell")

        self.verticalLayout_2.addWidget(self.ht_cell)


        self.retranslateUi(Dialog_item)

        QMetaObject.connectSlotsByName(Dialog_item)
    # setupUi

    def retranslateUi(self, Dialog_item):
        Dialog_item.setWindowTitle(QCoreApplication.translate("Dialog_item", u"Form", None))
        self.label.setText(QCoreApplication.translate("Dialog_item", u"TextLabel", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog_item", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog_item", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog_item", u"PushButton", None))
    # retranslateUi

