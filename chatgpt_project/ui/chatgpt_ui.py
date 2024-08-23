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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titlebar_layout = QWidget(self.centralwidget)
        self.titlebar_layout.setObjectName(u"titlebar_layout")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.titlebar_layout.sizePolicy().hasHeightForWidth())
        self.titlebar_layout.setSizePolicy(sizePolicy1)
        self.titlebar_layout.setMinimumSize(QSize(0, 36))
        self.titlebar_layout.setMaximumSize(QSize(16777215, 36))
        self.t = QHBoxLayout(self.titlebar_layout)
        self.t.setSpacing(2)
        self.t.setObjectName(u"t")
        self.t.setContentsMargins(3, 3, 3, 3)
        self.logo_label = QLabel(self.titlebar_layout)
        self.logo_label.setObjectName(u"logo_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.logo_label.sizePolicy().hasHeightForWidth())
        self.logo_label.setSizePolicy(sizePolicy2)
        self.logo_label.setMinimumSize(QSize(40, 30))
        self.logo_label.setMaximumSize(QSize(40, 30))

        self.t.addWidget(self.logo_label)

        self.label_2 = QLabel(self.titlebar_layout)
        self.label_2.setObjectName(u"label_2")

        self.t.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.t.addItem(self.horizontalSpacer)

        self.pin_btn = QPushButton(self.titlebar_layout)
        self.pin_btn.setObjectName(u"pin_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pin_btn.sizePolicy().hasHeightForWidth())
        self.pin_btn.setSizePolicy(sizePolicy3)
        self.pin_btn.setMinimumSize(QSize(30, 0))
        self.pin_btn.setMaximumSize(QSize(30, 16777215))
        font1 = QFont()
        font1.setPointSize(16)
        self.pin_btn.setFont(font1)
        icon = QIcon()
        icon.addFile(u"icon/pinoff.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u"icon/pin.png", QSize(), QIcon.Normal, QIcon.On)
        self.pin_btn.setIcon(icon)
        self.pin_btn.setIconSize(QSize(30, 30))
        self.pin_btn.setCheckable(True)

        self.t.addWidget(self.pin_btn)

        self.min_btn = QPushButton(self.titlebar_layout)
        self.min_btn.setObjectName(u"min_btn")
        sizePolicy2.setHeightForWidth(self.min_btn.sizePolicy().hasHeightForWidth())
        self.min_btn.setSizePolicy(sizePolicy2)
        self.min_btn.setMinimumSize(QSize(30, 0))
        self.min_btn.setMaximumSize(QSize(30, 100))

        self.t.addWidget(self.min_btn)

        self.max_btn = QPushButton(self.titlebar_layout)
        self.max_btn.setObjectName(u"max_btn")
        sizePolicy2.setHeightForWidth(self.max_btn.sizePolicy().hasHeightForWidth())
        self.max_btn.setSizePolicy(sizePolicy2)
        self.max_btn.setMinimumSize(QSize(30, 0))
        self.max_btn.setMaximumSize(QSize(30, 100))
        self.max_btn.setCheckable(True)

        self.t.addWidget(self.max_btn)

        self.exit_btn = QPushButton(self.titlebar_layout)
        self.exit_btn.setObjectName(u"exit_btn")
        sizePolicy2.setHeightForWidth(self.exit_btn.sizePolicy().hasHeightForWidth())
        self.exit_btn.setSizePolicy(sizePolicy2)
        self.exit_btn.setMinimumSize(QSize(30, 0))
        self.exit_btn.setMaximumSize(QSize(30, 100))

        self.t.addWidget(self.exit_btn)


        self.verticalLayout.addWidget(self.titlebar_layout)

        self.main_window = QWidget(self.centralwidget)
        self.main_window.setObjectName(u"main_window")
        self.main_window_layout = QHBoxLayout(self.main_window)
        self.main_window_layout.setSpacing(20)
        self.main_window_layout.setObjectName(u"main_window_layout")
        self.main_window_layout.setContentsMargins(20, 10, 10, 10)
        self.menu_wit = QWidget(self.main_window)
        self.menu_wit.setObjectName(u"menu_wit")
        self.menu_wit.setMinimumSize(QSize(200, 0))
        self.menu_wit.setMaximumSize(QSize(200, 16777215))
        self.menu_vlayout = QVBoxLayout(self.menu_wit)
        self.menu_vlayout.setSpacing(5)
        self.menu_vlayout.setObjectName(u"menu_vlayout")
        self.menu_vlayout.setContentsMargins(0, 0, 0, 0)
        self.dialog_ops_btn_layout = QHBoxLayout()
        self.dialog_ops_btn_layout.setSpacing(5)
        self.dialog_ops_btn_layout.setObjectName(u"dialog_ops_btn_layout")
        self.new_dialog_btn = QPushButton(self.menu_wit)
        self.new_dialog_btn.setObjectName(u"new_dialog_btn")
        self.new_dialog_btn.setMinimumSize(QSize(0, 36))
        self.new_dialog_btn.setMaximumSize(QSize(16777215, 36))

        self.dialog_ops_btn_layout.addWidget(self.new_dialog_btn)

        self.del_dialog_btn = QPushButton(self.menu_wit)
        self.del_dialog_btn.setObjectName(u"del_dialog_btn")
        self.del_dialog_btn.setMinimumSize(QSize(0, 36))
        self.del_dialog_btn.setMaximumSize(QSize(16777215, 36))

        self.dialog_ops_btn_layout.addWidget(self.del_dialog_btn)


        self.menu_vlayout.addLayout(self.dialog_ops_btn_layout)

        self.dialog_list_widget = QListWidget(self.menu_wit)
        self.dialog_list_widget.setObjectName(u"dialog_list_widget")
        self.dialog_list_widget.setFont(font)

        self.menu_vlayout.addWidget(self.dialog_list_widget)


        self.main_window_layout.addWidget(self.menu_wit)

        self.content_wit = QWidget(self.main_window)
        self.content_wit.setObjectName(u"content_wit")
        self.content_vlayout = QVBoxLayout(self.content_wit)
        self.content_vlayout.setSpacing(5)
        self.content_vlayout.setObjectName(u"content_vlayout")
        self.content_vlayout.setContentsMargins(0, 0, 0, 0)
        self.log_layout_w = QWidget(self.content_wit)
        self.log_layout_w.setObjectName(u"log_layout_w")
        sizePolicy1.setHeightForWidth(self.log_layout_w.sizePolicy().hasHeightForWidth())
        self.log_layout_w.setSizePolicy(sizePolicy1)
        self.log_layout_w.setMinimumSize(QSize(0, 36))
        self.log_layout_w.setMaximumSize(QSize(16777215, 36))
        self.log_layout = QHBoxLayout(self.log_layout_w)
        self.log_layout.setSpacing(2)
        self.log_layout.setObjectName(u"log_layout")
        self.log_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.log_layout.setContentsMargins(0, 0, 0, 0)
        self.param_name_lineedit = QLineEdit(self.log_layout_w)
        self.param_name_lineedit.setObjectName(u"param_name_lineedit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.param_name_lineedit.sizePolicy().hasHeightForWidth())
        self.param_name_lineedit.setSizePolicy(sizePolicy4)
        self.param_name_lineedit.setFont(font)
        self.param_name_lineedit.setFrame(False)

        self.log_layout.addWidget(self.param_name_lineedit)

        self.param_model_combo = QComboBox(self.log_layout_w)
        self.param_model_combo.addItem("")
        self.param_model_combo.addItem("")
        self.param_model_combo.addItem("")
        self.param_model_combo.setObjectName(u"param_model_combo")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.param_model_combo.sizePolicy().hasHeightForWidth())
        self.param_model_combo.setSizePolicy(sizePolicy5)
        self.param_model_combo.setMinimumSize(QSize(120, 0))
        self.param_model_combo.setMaximumSize(QSize(120, 16777215))
        self.param_model_combo.setFont(font)

        self.log_layout.addWidget(self.param_model_combo)

        self.param_temp_spin = QDoubleSpinBox(self.log_layout_w)
        self.param_temp_spin.setObjectName(u"param_temp_spin")
        sizePolicy5.setHeightForWidth(self.param_temp_spin.sizePolicy().hasHeightForWidth())
        self.param_temp_spin.setSizePolicy(sizePolicy5)
        self.param_temp_spin.setMinimumSize(QSize(110, 0))
        self.param_temp_spin.setMaximumSize(QSize(110, 16777215))
        self.param_temp_spin.setFont(font)
        self.param_temp_spin.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.param_temp_spin.setDecimals(1)
        self.param_temp_spin.setMaximum(2.000000000000000)
        self.param_temp_spin.setSingleStep(0.100000000000000)
        self.param_temp_spin.setValue(0.200000000000000)

        self.log_layout.addWidget(self.param_temp_spin)

        self.param_topp_spin = QDoubleSpinBox(self.log_layout_w)
        self.param_topp_spin.setObjectName(u"param_topp_spin")
        sizePolicy5.setHeightForWidth(self.param_topp_spin.sizePolicy().hasHeightForWidth())
        self.param_topp_spin.setSizePolicy(sizePolicy5)
        self.param_topp_spin.setMinimumSize(QSize(110, 0))
        self.param_topp_spin.setMaximumSize(QSize(110, 16777215))
        self.param_topp_spin.setFont(font)
        self.param_topp_spin.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.param_topp_spin.setDecimals(1)
        self.param_topp_spin.setMaximum(1.000000000000000)
        self.param_topp_spin.setSingleStep(0.100000000000000)
        self.param_topp_spin.setValue(0.300000000000000)

        self.log_layout.addWidget(self.param_topp_spin)

        self.param_topk_spin = QDoubleSpinBox(self.log_layout_w)
        self.param_topk_spin.setObjectName(u"param_topk_spin")
        sizePolicy5.setHeightForWidth(self.param_topk_spin.sizePolicy().hasHeightForWidth())
        self.param_topk_spin.setSizePolicy(sizePolicy5)
        self.param_topk_spin.setMinimumSize(QSize(110, 0))
        self.param_topk_spin.setMaximumSize(QSize(110, 16777215))
        self.param_topk_spin.setFont(font)
        self.param_topk_spin.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.param_topk_spin.setDecimals(0)
        self.param_topk_spin.setMaximum(100.000000000000000)
        self.param_topk_spin.setSingleStep(1.000000000000000)
        self.param_topk_spin.setValue(30.000000000000000)

        self.log_layout.addWidget(self.param_topk_spin)


        self.content_vlayout.addWidget(self.log_layout_w)

        self.token_disp_layout_w = QWidget(self.content_wit)
        self.token_disp_layout_w.setObjectName(u"token_disp_layout_w")
        sizePolicy1.setHeightForWidth(self.token_disp_layout_w.sizePolicy().hasHeightForWidth())
        self.token_disp_layout_w.setSizePolicy(sizePolicy1)
        self.token_disp_layout_w.setMinimumSize(QSize(0, 30))
        self.token_disp_layout_w.setMaximumSize(QSize(16777215, 30))
        self.token_disp_layout_w.setBaseSize(QSize(0, 16))
        self.horizontalLayout_3 = QHBoxLayout(self.token_disp_layout_w)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.dialog_token_label = QLabel(self.token_disp_layout_w)
        self.dialog_token_label.setObjectName(u"dialog_token_label")
        font2 = QFont()
        font2.setPointSize(10)
        self.dialog_token_label.setFont(font2)
        self.dialog_token_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.dialog_token_label)

        self.horizontalLayout_3.setStretch(0, 2)

        self.content_vlayout.addWidget(self.token_disp_layout_w)

        self.dialog_widget = DialogList(self.content_wit)
        self.dialog_widget.setObjectName(u"dialog_widget")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.dialog_widget.sizePolicy().hasHeightForWidth())
        self.dialog_widget.setSizePolicy(sizePolicy6)
        self.dialog_widget.setMinimumSize(QSize(0, 300))

        self.content_vlayout.addWidget(self.dialog_widget)

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
        sizePolicy4.setHeightForWidth(self.system_edit.sizePolicy().hasHeightForWidth())
        self.system_edit.setSizePolicy(sizePolicy4)
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
        icon1 = QIcon()
        icon1.addFile(u"icon/up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.system_size_btn.setIcon(icon1)
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
        sizePolicy4.setHeightForWidth(self.input_edit.sizePolicy().hasHeightForWidth())
        self.input_edit.setSizePolicy(sizePolicy4)
        self.input_edit.setMinimumSize(QSize(0, 120))
        self.input_edit.setFont(font)

        self.horizontalLayout_2.addWidget(self.input_edit)

        self.button_layout_w = QWidget(self.input_layout_w)
        self.button_layout_w.setObjectName(u"button_layout_w")
        sizePolicy3.setHeightForWidth(self.button_layout_w.sizePolicy().hasHeightForWidth())
        self.button_layout_w.setSizePolicy(sizePolicy3)
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
        self.input_size_btn.setIcon(icon1)
        self.input_size_btn.setIconSize(QSize(30, 30))
        self.input_size_btn.setCheckable(True)

        self.verticalLayout_2.addWidget(self.input_size_btn)

        self.send_btn = QPushButton(self.button_layout_w)
        self.send_btn.setObjectName(u"send_btn")
        sizePolicy3.setHeightForWidth(self.send_btn.sizePolicy().hasHeightForWidth())
        self.send_btn.setSizePolicy(sizePolicy3)
        self.send_btn.setMinimumSize(QSize(0, 0))
        self.send_btn.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u"icon/send.png", QSize(), QIcon.Normal, QIcon.Off)
        self.send_btn.setIcon(icon2)
        self.send_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.send_btn)


        self.horizontalLayout_2.addWidget(self.button_layout_w)


        self.content_vlayout.addWidget(self.input_layout_w)


        self.main_window_layout.addWidget(self.content_wit)


        self.verticalLayout.addWidget(self.main_window)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u521b\u65b0\u7814\u53d1\u90e8", None))
#if QT_CONFIG(tooltip)
        self.pin_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u7a97\u4f53\u7f6e\u9876</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pin_btn.setText("")
        self.min_btn.setText("")
        self.max_btn.setText("")
#if QT_CONFIG(tooltip)
        self.exit_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.exit_btn.setText("")
        self.new_dialog_btn.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5bf9\u8bdd", None))
        self.del_dialog_btn.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u5bf9\u8bdd", None))
        self.param_name_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u65e5\u5fd7\u540d\u79f0", None))
        self.param_model_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"qwen-turbo", None))
        self.param_model_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"qwen-plus", None))
        self.param_model_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"qwen-max", None))

        self.param_temp_spin.setPrefix(QCoreApplication.translate("MainWindow", u"Temp=", None))
        self.param_topp_spin.setPrefix(QCoreApplication.translate("MainWindow", u"Top_P=", None))
        self.param_topk_spin.setPrefix(QCoreApplication.translate("MainWindow", u"Top_K=", None))
        self.dialog_token_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
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
        pass
    # retranslateUi

