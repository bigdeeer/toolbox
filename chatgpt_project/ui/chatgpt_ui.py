# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chatgpt_ui.ui'
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
    QListWidget, QListWidgetItem, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

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
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"../icon/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(24, 22))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.menu_wit = QWidget(self.centralwidget)
        self.menu_wit.setObjectName(u"menu_wit")
        self.menu_wit.setMinimumSize(QSize(140, 0))
        self.menu_wit.setMaximumSize(QSize(180, 16777215))
        self.menu_vlayout = QVBoxLayout(self.menu_wit)
        self.menu_vlayout.setSpacing(5)
        self.menu_vlayout.setObjectName(u"menu_vlayout")
        self.menu_vlayout.setContentsMargins(0, 0, 0, 0)
        self.dialog_names_list = QListWidget(self.menu_wit)
        self.dialog_names_list.setObjectName(u"dialog_names_list")
        self.dialog_names_list.setFont(font)

        self.menu_vlayout.addWidget(self.dialog_names_list)

        self.new_dialog_btn = QPushButton(self.menu_wit)
        self.new_dialog_btn.setObjectName(u"new_dialog_btn")
        self.new_dialog_btn.setMinimumSize(QSize(0, 36))
        self.new_dialog_btn.setMaximumSize(QSize(16777215, 36))
        self.new_dialog_btn.setFont(font)

        self.menu_vlayout.addWidget(self.new_dialog_btn)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.menu_vlayout.addItem(self.verticalSpacer_3)


        self.horizontalLayout_4.addWidget(self.menu_wit)

        self.content_wit = QWidget(self.centralwidget)
        self.content_wit.setObjectName(u"content_wit")
        self.content_vlayout = QVBoxLayout(self.content_wit)
        self.content_vlayout.setSpacing(5)
        self.content_vlayout.setObjectName(u"content_vlayout")
        self.content_vlayout.setContentsMargins(0, 0, 0, 0)
        self.log_layout_w = QWidget(self.content_wit)
        self.log_layout_w.setObjectName(u"log_layout_w")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.log_layout_w.sizePolicy().hasHeightForWidth())
        self.log_layout_w.setSizePolicy(sizePolicy1)
        self.log_layout_w.setMinimumSize(QSize(0, 36))
        self.log_layout_w.setMaximumSize(QSize(16777215, 36))
        self.log_layout = QHBoxLayout(self.log_layout_w)
        self.log_layout.setSpacing(2)
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
        self.log_name_edit.setFont(font)

        self.log_layout.addWidget(self.log_name_edit)

        self.model_combo = QComboBox(self.log_layout_w)
        self.model_combo.addItem("")
        self.model_combo.addItem("")
        self.model_combo.addItem("")
        self.model_combo.addItem("")
        self.model_combo.setObjectName(u"model_combo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.model_combo.sizePolicy().hasHeightForWidth())
        self.model_combo.setSizePolicy(sizePolicy3)
        self.model_combo.setFont(font)

        self.log_layout.addWidget(self.model_combo)

        self.temp_vbox = QDoubleSpinBox(self.log_layout_w)
        self.temp_vbox.setObjectName(u"temp_vbox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.temp_vbox.sizePolicy().hasHeightForWidth())
        self.temp_vbox.setSizePolicy(sizePolicy4)
        self.temp_vbox.setMinimumSize(QSize(140, 0))
        self.temp_vbox.setFont(font)
        self.temp_vbox.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.temp_vbox.setDecimals(1)
        self.temp_vbox.setMaximum(1.000000000000000)
        self.temp_vbox.setSingleStep(0.100000000000000)

        self.log_layout.addWidget(self.temp_vbox)

        self.topp_vbox = QDoubleSpinBox(self.log_layout_w)
        self.topp_vbox.setObjectName(u"topp_vbox")
        sizePolicy4.setHeightForWidth(self.topp_vbox.sizePolicy().hasHeightForWidth())
        self.topp_vbox.setSizePolicy(sizePolicy4)
        self.topp_vbox.setMinimumSize(QSize(140, 0))
        self.topp_vbox.setFont(font)
        self.topp_vbox.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.topp_vbox.setDecimals(1)
        self.topp_vbox.setMaximum(1.000000000000000)
        self.topp_vbox.setSingleStep(0.100000000000000)

        self.log_layout.addWidget(self.topp_vbox)

        self.save_btn = QPushButton(self.log_layout_w)
        self.save_btn.setObjectName(u"save_btn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy5)
        self.save_btn.setMinimumSize(QSize(36, 0))
        self.save_btn.setMaximumSize(QSize(36, 16777215))
        font1 = QFont()
        font1.setPointSize(16)
        self.save_btn.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u"icon/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_btn.setIcon(icon1)
        self.save_btn.setIconSize(QSize(30, 30))

        self.log_layout.addWidget(self.save_btn)

        self.load_btn = QPushButton(self.log_layout_w)
        self.load_btn.setObjectName(u"load_btn")
        sizePolicy5.setHeightForWidth(self.load_btn.sizePolicy().hasHeightForWidth())
        self.load_btn.setSizePolicy(sizePolicy5)
        self.load_btn.setMinimumSize(QSize(36, 0))
        self.load_btn.setMaximumSize(QSize(36, 16777215))
        self.load_btn.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u"icon/load.png", QSize(), QIcon.Normal, QIcon.Off)
        self.load_btn.setIcon(icon2)
        self.load_btn.setIconSize(QSize(30, 30))

        self.log_layout.addWidget(self.load_btn)

        self.pin_btn = QPushButton(self.log_layout_w)
        self.pin_btn.setObjectName(u"pin_btn")
        sizePolicy5.setHeightForWidth(self.pin_btn.sizePolicy().hasHeightForWidth())
        self.pin_btn.setSizePolicy(sizePolicy5)
        self.pin_btn.setMinimumSize(QSize(36, 0))
        self.pin_btn.setMaximumSize(QSize(36, 16777215))
        self.pin_btn.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u"icon/pinoff.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u"icon/pin.png", QSize(), QIcon.Normal, QIcon.On)
        self.pin_btn.setIcon(icon3)
        self.pin_btn.setIconSize(QSize(30, 30))
        self.pin_btn.setCheckable(True)

        self.log_layout.addWidget(self.pin_btn)


        self.content_vlayout.addWidget(self.log_layout_w)

        self.token_disp_layout_w = QWidget(self.content_wit)
        self.token_disp_layout_w.setObjectName(u"token_disp_layout_w")
        sizePolicy1.setHeightForWidth(self.token_disp_layout_w.sizePolicy().hasHeightForWidth())
        self.token_disp_layout_w.setSizePolicy(sizePolicy1)
        self.token_disp_layout_w.setMinimumSize(QSize(0, 36))
        self.token_disp_layout_w.setMaximumSize(QSize(16777215, 36))
        self.token_disp_layout_w.setBaseSize(QSize(0, 20))
        self.horizontalLayout_3 = QHBoxLayout(self.token_disp_layout_w)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.actual_token_disp = QLabel(self.token_disp_layout_w)
        self.actual_token_disp.setObjectName(u"actual_token_disp")
        self.actual_token_disp.setFont(font)

        self.horizontalLayout_3.addWidget(self.actual_token_disp)

        self.sum_token_disp = QLabel(self.token_disp_layout_w)
        self.sum_token_disp.setObjectName(u"sum_token_disp")
        self.sum_token_disp.setFont(font)

        self.horizontalLayout_3.addWidget(self.sum_token_disp)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 2)

        self.content_vlayout.addWidget(self.token_disp_layout_w)

        self.dialog_list = DialogList(self.content_wit)
        self.dialog_list.setObjectName(u"dialog_list")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.dialog_list.sizePolicy().hasHeightForWidth())
        self.dialog_list.setSizePolicy(sizePolicy6)
        self.dialog_list.setMinimumSize(QSize(0, 300))

        self.content_vlayout.addWidget(self.dialog_list)

        self.system_layout_w = QWidget(self.content_wit)
        self.system_layout_w.setObjectName(u"system_layout_w")
        sizePolicy6.setHeightForWidth(self.system_layout_w.sizePolicy().hasHeightForWidth())
        self.system_layout_w.setSizePolicy(sizePolicy6)
        self.system_layout_w.setMinimumSize(QSize(0, 36))
        self.horizontalLayout = QHBoxLayout(self.system_layout_w)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.system_edit = QPlainTextEdit(self.system_layout_w)
        self.system_edit.setObjectName(u"system_edit")
        sizePolicy2.setHeightForWidth(self.system_edit.sizePolicy().hasHeightForWidth())
        self.system_edit.setSizePolicy(sizePolicy2)
        self.system_edit.setFont(font)

        self.horizontalLayout.addWidget(self.system_edit)

        self.verticalWidget = QWidget(self.system_layout_w)
        self.verticalWidget.setObjectName(u"verticalWidget")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy7)
        self.verticalWidget.setMinimumSize(QSize(36, 0))
        self.verticalWidget.setMaximumSize(QSize(36, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.system_size_btn = QPushButton(self.verticalWidget)
        self.system_size_btn.setObjectName(u"system_size_btn")
        sizePolicy.setHeightForWidth(self.system_size_btn.sizePolicy().hasHeightForWidth())
        self.system_size_btn.setSizePolicy(sizePolicy)
        self.system_size_btn.setMinimumSize(QSize(0, 36))
        self.system_size_btn.setMaximumSize(QSize(16777215, 36))
        self.system_size_btn.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u"icon/up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.system_size_btn.setIcon(icon4)
        self.system_size_btn.setIconSize(QSize(30, 30))
        self.system_size_btn.setCheckable(True)

        self.verticalLayout_3.addWidget(self.system_size_btn)

        self.verticalSpacer_2 = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.verticalWidget)


        self.content_vlayout.addWidget(self.system_layout_w)

        self.input_layout_w = QWidget(self.content_wit)
        self.input_layout_w.setObjectName(u"input_layout_w")
        sizePolicy6.setHeightForWidth(self.input_layout_w.sizePolicy().hasHeightForWidth())
        self.input_layout_w.setSizePolicy(sizePolicy6)
        self.input_layout_w.setMinimumSize(QSize(0, 120))
        self.horizontalLayout_2 = QHBoxLayout(self.input_layout_w)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.input_edit = QPlainTextEdit(self.input_layout_w)
        self.input_edit.setObjectName(u"input_edit")
        sizePolicy2.setHeightForWidth(self.input_edit.sizePolicy().hasHeightForWidth())
        self.input_edit.setSizePolicy(sizePolicy2)
        self.input_edit.setMinimumSize(QSize(0, 112))
        self.input_edit.setFont(font)

        self.horizontalLayout_2.addWidget(self.input_edit)

        self.button_layout_w = QWidget(self.input_layout_w)
        self.button_layout_w.setObjectName(u"button_layout_w")
        sizePolicy5.setHeightForWidth(self.button_layout_w.sizePolicy().hasHeightForWidth())
        self.button_layout_w.setSizePolicy(sizePolicy5)
        self.button_layout_w.setMinimumSize(QSize(36, 0))
        self.button_layout_w.setMaximumSize(QSize(36, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.button_layout_w)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.input_size_btn = QPushButton(self.button_layout_w)
        self.input_size_btn.setObjectName(u"input_size_btn")
        sizePolicy.setHeightForWidth(self.input_size_btn.sizePolicy().hasHeightForWidth())
        self.input_size_btn.setSizePolicy(sizePolicy)
        self.input_size_btn.setMinimumSize(QSize(0, 36))
        self.input_size_btn.setMaximumSize(QSize(16777215, 36))
        self.input_size_btn.setFont(font1)
        self.input_size_btn.setIcon(icon4)
        self.input_size_btn.setIconSize(QSize(30, 30))
        self.input_size_btn.setCheckable(True)

        self.verticalLayout_2.addWidget(self.input_size_btn)

        self.send_btn = QPushButton(self.button_layout_w)
        self.send_btn.setObjectName(u"send_btn")
        sizePolicy.setHeightForWidth(self.send_btn.sizePolicy().hasHeightForWidth())
        self.send_btn.setSizePolicy(sizePolicy)
        self.send_btn.setMinimumSize(QSize(0, 36))
        self.send_btn.setMaximumSize(QSize(16777215, 36))
        self.send_btn.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u"icon/send.png", QSize(), QIcon.Normal, QIcon.Off)
        self.send_btn.setIcon(icon5)
        self.send_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.send_btn)

        self.clear_btn = QPushButton(self.button_layout_w)
        self.clear_btn.setObjectName(u"clear_btn")
        sizePolicy.setHeightForWidth(self.clear_btn.sizePolicy().hasHeightForWidth())
        self.clear_btn.setSizePolicy(sizePolicy)
        self.clear_btn.setMinimumSize(QSize(0, 36))
        self.clear_btn.setMaximumSize(QSize(16777215, 36))
        self.clear_btn.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u"icon/clear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clear_btn.setIcon(icon6)
        self.clear_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.clear_btn)

        self.verticalSpacer = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.button_layout_w)


        self.content_vlayout.addWidget(self.input_layout_w)


        self.horizontalLayout_4.addWidget(self.content_wit)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Azure-openAI-GPT\u521b\u65b0\u7814\u53d1\u90e8", None))
        self.new_dialog_btn.setText(QCoreApplication.translate("MainWindow", u"New dialog", None))
        self.log_name_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u65e5\u5fd7\u540d\u79f0", None))
        self.model_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"qwen-turbo", None))
        self.model_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"3.5-4k", None))
        self.model_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"qwen-plus", None))
        self.model_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"qwen-max", None))

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
        self.actual_token_disp.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.sum_token_disp.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.system_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u80cc\u666f\u4fe1\u606f,Enter\u6362\u884c,Ctrl+\u2193\u5c55\u5f00/\u6536\u7f29\u8f93\u5165\u6846", None))
#if QT_CONFIG(tooltip)
        self.system_size_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u5c55\u5f00/\u6536\u7f29</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.system_size_btn.setText("")
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

