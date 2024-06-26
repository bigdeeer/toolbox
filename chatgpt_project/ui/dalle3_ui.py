# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dalle3_ui.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDoubleSpinBox,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from widgets.dialog_listwidget import DialogList

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(975, 678)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(40, 40))
        font = QFont()
        font.setPointSize(20)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(194, 204, 194);\n"
"border:1px solid rgb(90,90,90);\n"
"border-radius:6px;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.log_layout_w = QWidget(self.centralwidget)
        self.log_layout_w.setObjectName(u"log_layout_w")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.log_layout_w.sizePolicy().hasHeightForWidth())
        self.log_layout_w.setSizePolicy(sizePolicy1)
        self.log_layout_w.setStyleSheet(u"border:0px;")
        self.log_layout = QHBoxLayout(self.log_layout_w)
        self.log_layout.setSpacing(0)
        self.log_layout.setObjectName(u"log_layout")
        self.log_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.log_layout.setContentsMargins(0, 0, 0, 0)
        self.log_name_edit = QLineEdit(self.log_layout_w)
        self.log_name_edit.setObjectName(u"log_name_edit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.log_name_edit.sizePolicy().hasHeightForWidth())
        self.log_name_edit.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(12)
        self.log_name_edit.setFont(font1)
        self.log_name_edit.setStyleSheet(u"background-color:rgb(215,221,215);\n"
"border:1px solid rgb(90,90,90);\n"
"border-radius:4px;")

        self.log_layout.addWidget(self.log_name_edit)

        self.model_combo = QComboBox(self.log_layout_w)
        self.model_combo.addItem("")
        self.model_combo.addItem("")
        self.model_combo.setObjectName(u"model_combo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.model_combo.sizePolicy().hasHeightForWidth())
        self.model_combo.setSizePolicy(sizePolicy3)
        self.model_combo.setMinimumSize(QSize(70, 0))
        self.model_combo.setStyleSheet(u"background-color:rgb(215,221,215);\n"
"border:1px solid rgb(90,90,90);\n"
"border-radius:4px;")

        self.log_layout.addWidget(self.model_combo)

        self.temp_vbox = QDoubleSpinBox(self.log_layout_w)
        self.temp_vbox.setObjectName(u"temp_vbox")
        sizePolicy3.setHeightForWidth(self.temp_vbox.sizePolicy().hasHeightForWidth())
        self.temp_vbox.setSizePolicy(sizePolicy3)
        self.temp_vbox.setMinimumSize(QSize(100, 0))
        self.temp_vbox.setStyleSheet(u"background-color:rgb(215,221,215);\n"
"border:1px solid rgb(90,90,90);\n"
"border-radius:4px;")
        self.temp_vbox.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.temp_vbox.setDecimals(1)
        self.temp_vbox.setMaximum(1.000000000000000)
        self.temp_vbox.setSingleStep(0.100000000000000)

        self.log_layout.addWidget(self.temp_vbox)

        self.topp_vbox = QDoubleSpinBox(self.log_layout_w)
        self.topp_vbox.setObjectName(u"topp_vbox")
        sizePolicy3.setHeightForWidth(self.topp_vbox.sizePolicy().hasHeightForWidth())
        self.topp_vbox.setSizePolicy(sizePolicy3)
        self.topp_vbox.setMinimumSize(QSize(100, 0))
        self.topp_vbox.setStyleSheet(u"background-color:rgb(215,221,215);\n"
"border:1px solid rgb(90,90,90);\n"
"border-radius:4px;")
        self.topp_vbox.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.topp_vbox.setDecimals(1)
        self.topp_vbox.setMaximum(1.000000000000000)
        self.topp_vbox.setSingleStep(0.100000000000000)

        self.log_layout.addWidget(self.topp_vbox)

        self.save_btn = QPushButton(self.log_layout_w)
        self.save_btn.setObjectName(u"save_btn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy4)
        self.save_btn.setMinimumSize(QSize(40, 0))
        font2 = QFont()
        font2.setPointSize(16)
        self.save_btn.setFont(font2)
        self.save_btn.setStyleSheet(u"QPushButton:checked\n"
"{\n"
"background-color: rgb(165,180,165)\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color:rgb(215,221,215);\n"
"border:1px solid rgb(90,90,90);\n"
"border-radius:4px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(238,232,210)\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(105,158,105)\n"
"}")
        icon = QIcon()
        icon.addFile(u"icon/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_btn.setIcon(icon)
        self.save_btn.setIconSize(QSize(30, 30))

        self.log_layout.addWidget(self.save_btn)

        self.load_btn = QPushButton(self.log_layout_w)
        self.load_btn.setObjectName(u"load_btn")
        sizePolicy4.setHeightForWidth(self.load_btn.sizePolicy().hasHeightForWidth())
        self.load_btn.setSizePolicy(sizePolicy4)
        self.load_btn.setMinimumSize(QSize(40, 0))
        self.load_btn.setFont(font2)
        self.load_btn.setStyleSheet(u"QPushButton:checked\n"
"{\n"
"background-color: rgb(165,180,165)\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color:rgb(215,221,215);\n"
"border:1px solid rgb(90,90,90);\n"
"border-radius:4px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(238,232,210)\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(105,158,105)\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icon/load.png", QSize(), QIcon.Normal, QIcon.Off)
        self.load_btn.setIcon(icon1)
        self.load_btn.setIconSize(QSize(30, 30))

        self.log_layout.addWidget(self.load_btn)

        self.pin_btn = QPushButton(self.log_layout_w)
        self.pin_btn.setObjectName(u"pin_btn")
        sizePolicy4.setHeightForWidth(self.pin_btn.sizePolicy().hasHeightForWidth())
        self.pin_btn.setSizePolicy(sizePolicy4)
        self.pin_btn.setMinimumSize(QSize(40, 0))
        self.pin_btn.setFont(font2)
        self.pin_btn.setStyleSheet(u"QPushButton:checked\n"
"{\n"
"background-color: rgb(165,180,165)\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color:rgb(215,221,215);\n"
"border:1px solid rgb(90,90,90);\n"
"border-radius:4px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(238,232,210)\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(105,158,105)\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icon/pinoff.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u"icon/pin.png", QSize(), QIcon.Normal, QIcon.On)
        self.pin_btn.setIcon(icon2)
        self.pin_btn.setIconSize(QSize(30, 30))
        self.pin_btn.setCheckable(True)

        self.log_layout.addWidget(self.pin_btn)


        self.verticalLayout.addWidget(self.log_layout_w)

        self.token_disp_layout_w = QWidget(self.centralwidget)
        self.token_disp_layout_w.setObjectName(u"token_disp_layout_w")
        self.token_disp_layout_w.setStyleSheet(u"border:0px;")
        self.horizontalLayout_3 = QHBoxLayout(self.token_disp_layout_w)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.predicted_token_disp = QLabel(self.token_disp_layout_w)
        self.predicted_token_disp.setObjectName(u"predicted_token_disp")
        self.predicted_token_disp.setFont(font1)

        self.horizontalLayout_3.addWidget(self.predicted_token_disp)

        self.actual_token_disp = QLabel(self.token_disp_layout_w)
        self.actual_token_disp.setObjectName(u"actual_token_disp")
        self.actual_token_disp.setFont(font1)

        self.horizontalLayout_3.addWidget(self.actual_token_disp)

        self.sum_token_disp = QLabel(self.token_disp_layout_w)
        self.sum_token_disp.setObjectName(u"sum_token_disp")
        self.sum_token_disp.setFont(font1)

        self.horizontalLayout_3.addWidget(self.sum_token_disp)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 2)

        self.verticalLayout.addWidget(self.token_disp_layout_w)

        self.dialog_list = DialogList(self.centralwidget)
        self.dialog_list.setObjectName(u"dialog_list")
        sizePolicy2.setHeightForWidth(self.dialog_list.sizePolicy().hasHeightForWidth())
        self.dialog_list.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.dialog_list)

        self.input_layout_w = QWidget(self.centralwidget)
        self.input_layout_w.setObjectName(u"input_layout_w")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.input_layout_w.sizePolicy().hasHeightForWidth())
        self.input_layout_w.setSizePolicy(sizePolicy5)
        self.input_layout_w.setStyleSheet(u"border:0px")
        self.horizontalLayout_2 = QHBoxLayout(self.input_layout_w)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.input_edit = QPlainTextEdit(self.input_layout_w)
        self.input_edit.setObjectName(u"input_edit")
        sizePolicy2.setHeightForWidth(self.input_edit.sizePolicy().hasHeightForWidth())
        self.input_edit.setSizePolicy(sizePolicy2)
        self.input_edit.setFont(font)
        self.input_edit.setStyleSheet(u"background-color:rgb(220,225,230);\n"
"border:1px solid rgb(90,90,90);\n"
"border-radius:4px;")

        self.horizontalLayout_2.addWidget(self.input_edit)

        self.button_layout_w = QWidget(self.input_layout_w)
        self.button_layout_w.setObjectName(u"button_layout_w")
        sizePolicy4.setHeightForWidth(self.button_layout_w.sizePolicy().hasHeightForWidth())
        self.button_layout_w.setSizePolicy(sizePolicy4)
        self.button_layout_w.setStyleSheet(u"border:0px")
        self.verticalLayout_2 = QVBoxLayout(self.button_layout_w)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.input_size_btn = QPushButton(self.button_layout_w)
        self.input_size_btn.setObjectName(u"input_size_btn")
        sizePolicy.setHeightForWidth(self.input_size_btn.sizePolicy().hasHeightForWidth())
        self.input_size_btn.setSizePolicy(sizePolicy)
        self.input_size_btn.setFont(font2)
        self.input_size_btn.setStyleSheet(u"QPushButton:checked\n"
"{\n"
"background-color: rgb(165,180,165)\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color:rgb(215,221,215);\n"
"border:1px solid rgb(90,90,90);\n"
"border-radius:4px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(238,232,210)\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(105,158,105)\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"icon/up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.input_size_btn.setIcon(icon3)
        self.input_size_btn.setIconSize(QSize(30, 30))
        self.input_size_btn.setCheckable(True)

        self.verticalLayout_2.addWidget(self.input_size_btn)

        self.send_btn = QPushButton(self.button_layout_w)
        self.send_btn.setObjectName(u"send_btn")
        sizePolicy.setHeightForWidth(self.send_btn.sizePolicy().hasHeightForWidth())
        self.send_btn.setSizePolicy(sizePolicy)
        self.send_btn.setFont(font2)
        self.send_btn.setStyleSheet(u"QPushButton:checked\n"
"{\n"
"background-color: rgb(165,180,165)\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color:rgb(215,221,215);\n"
"border:1px solid rgb(90,90,90);\n"
"border-radius:4px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(238,232,210)\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(105,158,105)\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"icon/send.png", QSize(), QIcon.Normal, QIcon.Off)
        self.send_btn.setIcon(icon4)
        self.send_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.send_btn)

        self.clear_btn = QPushButton(self.button_layout_w)
        self.clear_btn.setObjectName(u"clear_btn")
        sizePolicy.setHeightForWidth(self.clear_btn.sizePolicy().hasHeightForWidth())
        self.clear_btn.setSizePolicy(sizePolicy)
        self.clear_btn.setFont(font2)
        self.clear_btn.setStyleSheet(u"QPushButton:checked\n"
"{\n"
"background-color: rgb(165,180,165)\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color:rgb(215,221,215);\n"
"border:1px solid rgb(90,90,90);\n"
"border-radius:4px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(238,232,210)\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(105,158,105)\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"icon/clear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clear_btn.setIcon(icon5)
        self.clear_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.clear_btn)

        self.verticalSpacer = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.button_layout_w)


        self.verticalLayout.addWidget(self.input_layout_w)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("")
        self.log_name_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u540d\u79f0", None))
        self.model_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"3.5-4k", None))
        self.model_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"3.5-16K", None))

        self.temp_vbox.setPrefix(QCoreApplication.translate("MainWindow", u" Temp = ", None))
        self.topp_vbox.setPrefix(QCoreApplication.translate("MainWindow", u" Top_P = ", None))
#if QT_CONFIG(tooltip)
        self.save_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u4fdd\u5b58\u65e5\u5fd7</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.save_btn.setText("")
#if QT_CONFIG(tooltip)
        self.load_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u52a0\u8f7d\u65e5\u5fd7</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.load_btn.setText("")
#if QT_CONFIG(tooltip)
        self.pin_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u7a97\u4f53\u7f6e\u9876</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pin_btn.setText("")
        self.predicted_token_disp.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.actual_token_disp.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.sum_token_disp.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.input_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter\u6362\u884c\uff0cCtrl+Enter\u53d1\u9001\uff0cCtrl+\u2191\u5c55\u5f00/\u6536\u7f29\u8f93\u5165\u6846", None))
#if QT_CONFIG(tooltip)
        self.input_size_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u5c55\u5f00/\u6536\u7f29</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.input_size_btn.setText("")
#if QT_CONFIG(tooltip)
        self.send_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u53d1\u9001</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.send_btn.setText("")
#if QT_CONFIG(tooltip)
        self.clear_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u6e05\u7a7a</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.clear_btn.setText("")
    # retranslateUi

