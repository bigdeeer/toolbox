# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'youtubedlUI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHeaderView,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 900)
        MainWindow.setMaximumSize(QSize(800, 900))
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.parse_button = QPushButton(self.centralwidget)
        self.parse_button.setObjectName(u"parse_button")
        self.parse_button.setGeometry(QRect(680, 90, 111, 31))
        self.parse_button.setFont(font)
        self.parse_button.setStyleSheet(u"QPushButton:hover {background-color: rgb(80,60,60)}\n"
"QPushButton:pressed {background-color: rgb(240,160,190)}\n"
"QPushButton{color: rgb(255, 255, 255);\n"
"border:1px solid rgb(130, 130, 130) ;}")
        self.link_text = QLineEdit(self.centralwidget)
        self.link_text.setObjectName(u"link_text")
        self.link_text.setGeometry(QRect(10, 90, 661, 31))
        self.link_text.setFont(font)
        self.link_text.setStyleSheet(u"border:1px solid rgb(130, 130, 130) ;\n"
"color:white")
        self.link_text.setAlignment(Qt.AlignCenter)
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 9):
            self.tableWidget.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem9)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 130, 781, 731))
        self.tableWidget.setStyleSheet(u"QWidget{\n"
"background-color: transparent;\n"
"color:white;\n"
"gridline-color:rgb(40,40,40);\n"
"}\n"
"QHeaderView::section{\n"
"background-color:transparent;\n"
"}\n"
"QTableCornerButton::section {\n"
"    background-color: transparent;\n"
"}")
        self.tableWidget.setFrameShape(QFrame.StyledPanel)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.ip_text = QLineEdit(self.centralwidget)
        self.ip_text.setObjectName(u"ip_text")
        self.ip_text.setGeometry(QRect(500, 10, 291, 31))
        self.ip_text.setFont(font)
        self.ip_text.setStyleSheet(u"border:1px solid rgb(130, 130, 130) ;\n"
"color:white")
        self.ip_text.setAlignment(Qt.AlignCenter)
        self.path_text = QLineEdit(self.centralwidget)
        self.path_text.setObjectName(u"path_text")
        self.path_text.setGeometry(QRect(10, 10, 391, 31))
        self.path_text.setFont(font)
        self.path_text.setStyleSheet(u"border:1px solid rgb(130, 130, 130) ;\n"
"color:white")
        self.path_text.setAlignment(Qt.AlignCenter)
        self.browse_button = QPushButton(self.centralwidget)
        self.browse_button.setObjectName(u"browse_button")
        self.browse_button.setGeometry(QRect(410, 10, 81, 31))
        self.browse_button.setFont(font)
        self.browse_button.setStyleSheet(u"QPushButton:hover {background-color: rgb(80,60,60)}\n"
"QPushButton:pressed {background-color: rgb(240,160,190)}\n"
"QPushButton{color: rgb(255, 255, 255);\n"
"border:1px solid rgb(130, 130, 130) ;}")
        self.playlist_button = QPushButton(self.centralwidget)
        self.playlist_button.setObjectName(u"playlist_button")
        self.playlist_button.setGeometry(QRect(500, 50, 161, 31))
        self.playlist_button.setFont(font)
        self.playlist_button.setStyleSheet(u"QPushButton:hover {background-color: rgb(80,60,60)}\n"
"QPushButton:pressed {background-color: rgb(240,160,190)}\n"
"QPushButton{color: rgb(255, 255, 255);\n"
"border:1px solid rgb(130, 130, 130) ;}")
        self.link2_text = QLineEdit(self.centralwidget)
        self.link2_text.setObjectName(u"link2_text")
        self.link2_text.setGeometry(QRect(10, 50, 481, 31))
        self.link2_text.setFont(font)
        self.link2_text.setStyleSheet(u"border:1px solid rgb(130, 130, 130) ;\n"
"color:white")
        self.link2_text.setAlignment(Qt.AlignCenter)
        self.merge_button = QPushButton(self.centralwidget)
        self.merge_button.setObjectName(u"merge_button")
        self.merge_button.setGeometry(QRect(670, 50, 121, 31))
        self.merge_button.setFont(font)
        self.merge_button.setStyleSheet(u"QPushButton:hover {background-color: rgb(80,60,60)}\n"
"QPushButton:pressed {background-color: rgb(240,160,190)}\n"
"QPushButton{color: rgb(255, 255, 255);\n"
"border:1px solid rgb(130, 130, 130) ;}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.status_text = QStatusBar(MainWindow)
        self.status_text.setObjectName(u"status_text")
        self.status_text.setFont(font)
        self.status_text.setStyleSheet(u"color: rgb(255, 255, 255);")
        MainWindow.setStatusBar(self.status_text)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Youtube download link parser", None))
        self.parse_button.setText(QCoreApplication.translate("MainWindow", u"Parse link", None))
        self.link_text.setText("")
        self.link_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Video link here", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Res", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Fps", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Ext", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Size(MB)", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Abr(kbps)", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Video codec", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Audio codec", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Link", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"IDM download", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
#if QT_CONFIG(tooltip)
        self.ip_text.setToolTip(QCoreApplication.translate("MainWindow", u"Http(s) proxy IP address", None))
#endif // QT_CONFIG(tooltip)
        self.ip_text.setText(QCoreApplication.translate("MainWindow", u"127.0.0.1", None))
        self.path_text.setText("")
        self.path_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Save path here", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.playlist_button.setText(QCoreApplication.translate("MainWindow", u"Download playlist", None))
        self.link2_text.setText(QCoreApplication.translate("MainWindow", u"https://www.youtube.com/watch?v=WCI6zGoXRdA&list=PLOYb5b_5Q-xr3n7Cvxg7eh_UC2Z2bVQVl", None))
        self.link2_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Playlist link here", None))
        self.merge_button.setText(QCoreApplication.translate("MainWindow", u"Merge meta", None))
    # retranslateUi

