# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gps_qt_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

from widgets.map_widget import MapWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.resize(860, 786)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(40, 40))
        MainWindow.setContextMenuPolicy(Qt.PreventContextMenu)
        icon = QIcon(QIcon.fromTheme(u"camera-video"))
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        MainWindow.setIconSize(QSize(24, 22))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.map_widget = MapWidget(self.centralwidget)
        self.map_widget.setObjectName(u"map_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.map_widget.sizePolicy().hasHeightForWidth())
        self.map_widget.setSizePolicy(sizePolicy1)
        self.map_widget.setStyleSheet(u"border:1px solid black")

        self.verticalLayout_2.addWidget(self.map_widget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.edit_poly_btn = QPushButton(self.centralwidget)
        self.edit_poly_btn.setObjectName(u"edit_poly_btn")

        self.horizontalLayout.addWidget(self.edit_poly_btn)

        self.restore_poly_btn = QPushButton(self.centralwidget)
        self.restore_poly_btn.setObjectName(u"restore_poly_btn")

        self.horizontalLayout.addWidget(self.restore_poly_btn)

        self.save_poly_btn = QPushButton(self.centralwidget)
        self.save_poly_btn.setObjectName(u"save_poly_btn")

        self.horizontalLayout.addWidget(self.save_poly_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("")
        self.edit_poly_btn.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91\u591a\u8fb9\u5f62", None))
        self.restore_poly_btn.setText(QCoreApplication.translate("MainWindow", u"\u590d\u539f\u591a\u8fb9\u5f62\u6570\u636e", None))
        self.save_poly_btn.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u591a\u8fb9\u5f62\u6570\u636e", None))
    # retranslateUi

