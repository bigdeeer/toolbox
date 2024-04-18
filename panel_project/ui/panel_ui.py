# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'panel_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSplitter, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(938, 2010)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setSizeIncrement(QSize(5, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_10 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(15)
        self.v_layout = QWidget(self.splitter)
        self.v_layout.setObjectName(u"v_layout")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.v_layout.sizePolicy().hasHeightForWidth())
        self.v_layout.setSizePolicy(sizePolicy1)
        self.v_layout.setMaximumSize(QSize(500, 16777215))
        self.verticalLayout_28 = QVBoxLayout(self.v_layout)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.horizontalWidget = QWidget(self.v_layout)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget = QWidget(self.horizontalWidget)
        self.verticalWidget.setObjectName(u"verticalWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy2)
        self.verticalWidget.setMinimumSize(QSize(50, 0))
        self.verticalLayout = QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.verticalWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 24))
        self.pushButton.setStyleSheet(u"border:1px solid black;\n"
"background-color: rgb(139, 186, 231);")

        self.verticalLayout.addWidget(self.pushButton)

        self.lineEdit = QLineEdit(self.verticalWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 24))
        self.lineEdit.setStyleSheet(u"border:1px solid black")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.verticalWidget)

        self.plainTextEdit = QPlainTextEdit(self.horizontalWidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setStyleSheet(u"border:1px solid black")

        self.horizontalLayout.addWidget(self.plainTextEdit)


        self.verticalLayout_28.addWidget(self.horizontalWidget)

        self.horizontalWidget_2 = QWidget(self.v_layout)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget_2 = QWidget(self.horizontalWidget_2)
        self.verticalWidget_2.setObjectName(u"verticalWidget_2")
        sizePolicy2.setHeightForWidth(self.verticalWidget_2.sizePolicy().hasHeightForWidth())
        self.verticalWidget_2.setSizePolicy(sizePolicy2)
        self.verticalWidget_2.setMinimumSize(QSize(50, 0))
        self.verticalLayout_2 = QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.verticalWidget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 24))
        self.pushButton_2.setStyleSheet(u"border:1px solid black;\n"
"background-color: rgb(139, 186, 231);")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.lineEdit_2 = QLineEdit(self.verticalWidget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 24))
        self.lineEdit_2.setStyleSheet(u"border:1px solid black")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addWidget(self.verticalWidget_2)

        self.plainTextEdit_2 = QPlainTextEdit(self.horizontalWidget_2)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setStyleSheet(u"border:1px solid black")

        self.horizontalLayout_2.addWidget(self.plainTextEdit_2)


        self.verticalLayout_28.addWidget(self.horizontalWidget_2)

        self.horizontalWidget_19 = QWidget(self.v_layout)
        self.horizontalWidget_19.setObjectName(u"horizontalWidget_19")
        self.horizontalLayout_23 = QHBoxLayout(self.horizontalWidget_19)
        self.horizontalLayout_23.setSpacing(5)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget_21 = QWidget(self.horizontalWidget_19)
        self.verticalWidget_21.setObjectName(u"verticalWidget_21")
        sizePolicy2.setHeightForWidth(self.verticalWidget_21.sizePolicy().hasHeightForWidth())
        self.verticalWidget_21.setSizePolicy(sizePolicy2)
        self.verticalWidget_21.setMinimumSize(QSize(50, 0))
        self.verticalLayout_24 = QVBoxLayout(self.verticalWidget_21)
        self.verticalLayout_24.setSpacing(5)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.pushButton_23 = QPushButton(self.verticalWidget_21)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setMinimumSize(QSize(0, 24))
        self.pushButton_23.setStyleSheet(u"border:1px solid black;\n"
"background-color: rgb(139, 186, 231);")

        self.verticalLayout_24.addWidget(self.pushButton_23)

        self.lineEdit_21 = QLineEdit(self.verticalWidget_21)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setMinimumSize(QSize(0, 24))
        self.lineEdit_21.setStyleSheet(u"border:1px solid black")
        self.lineEdit_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.lineEdit_21)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_21)


        self.horizontalLayout_23.addWidget(self.verticalWidget_21)

        self.plainTextEdit_21 = QPlainTextEdit(self.horizontalWidget_19)
        self.plainTextEdit_21.setObjectName(u"plainTextEdit_21")
        self.plainTextEdit_21.setStyleSheet(u"border:1px solid black")

        self.horizontalLayout_23.addWidget(self.plainTextEdit_21)


        self.verticalLayout_28.addWidget(self.horizontalWidget_19)

        self.horizontalWidget_16 = QWidget(self.v_layout)
        self.horizontalWidget_16.setObjectName(u"horizontalWidget_16")
        self.horizontalLayout_19 = QHBoxLayout(self.horizontalWidget_16)
        self.horizontalLayout_19.setSpacing(5)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget_17 = QWidget(self.horizontalWidget_16)
        self.verticalWidget_17.setObjectName(u"verticalWidget_17")
        sizePolicy2.setHeightForWidth(self.verticalWidget_17.sizePolicy().hasHeightForWidth())
        self.verticalWidget_17.setSizePolicy(sizePolicy2)
        self.verticalWidget_17.setMinimumSize(QSize(50, 0))
        self.verticalLayout_20 = QVBoxLayout(self.verticalWidget_17)
        self.verticalLayout_20.setSpacing(10)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.pushButton_19 = QPushButton(self.verticalWidget_17)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(0, 24))
        self.pushButton_19.setStyleSheet(u"border:1px solid black;\n"
"background-color: rgb(139, 186, 231);")

        self.verticalLayout_20.addWidget(self.pushButton_19)

        self.lineEdit_17 = QLineEdit(self.verticalWidget_17)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setMinimumSize(QSize(0, 24))
        self.lineEdit_17.setStyleSheet(u"border:1px solid black")
        self.lineEdit_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.lineEdit_17)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_17)


        self.horizontalLayout_19.addWidget(self.verticalWidget_17)

        self.plainTextEdit_17 = QPlainTextEdit(self.horizontalWidget_16)
        self.plainTextEdit_17.setObjectName(u"plainTextEdit_17")
        self.plainTextEdit_17.setStyleSheet(u"border:1px solid black")

        self.horizontalLayout_19.addWidget(self.plainTextEdit_17)


        self.verticalLayout_28.addWidget(self.horizontalWidget_16)

        self.horizontalWidget_20 = QWidget(self.v_layout)
        self.horizontalWidget_20.setObjectName(u"horizontalWidget_20")
        self.horizontalLayout_24 = QHBoxLayout(self.horizontalWidget_20)
        self.horizontalLayout_24.setSpacing(5)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget_22 = QWidget(self.horizontalWidget_20)
        self.verticalWidget_22.setObjectName(u"verticalWidget_22")
        sizePolicy2.setHeightForWidth(self.verticalWidget_22.sizePolicy().hasHeightForWidth())
        self.verticalWidget_22.setSizePolicy(sizePolicy2)
        self.verticalWidget_22.setMinimumSize(QSize(50, 0))
        self.verticalLayout_25 = QVBoxLayout(self.verticalWidget_22)
        self.verticalLayout_25.setSpacing(5)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.pushButton_24 = QPushButton(self.verticalWidget_22)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setMinimumSize(QSize(0, 24))
        self.pushButton_24.setStyleSheet(u"border:1px solid black;\n"
"background-color: rgb(139, 186, 231);")

        self.verticalLayout_25.addWidget(self.pushButton_24)

        self.lineEdit_22 = QLineEdit(self.verticalWidget_22)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setMinimumSize(QSize(0, 24))
        self.lineEdit_22.setStyleSheet(u"border:1px solid black")
        self.lineEdit_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.lineEdit_22)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_22)


        self.horizontalLayout_24.addWidget(self.verticalWidget_22)

        self.plainTextEdit_22 = QPlainTextEdit(self.horizontalWidget_20)
        self.plainTextEdit_22.setObjectName(u"plainTextEdit_22")
        self.plainTextEdit_22.setStyleSheet(u"border:1px solid black")

        self.horizontalLayout_24.addWidget(self.plainTextEdit_22)


        self.verticalLayout_28.addWidget(self.horizontalWidget_20)

        self.horizontalWidget_3 = QWidget(self.v_layout)
        self.horizontalWidget_3.setObjectName(u"horizontalWidget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget_3 = QWidget(self.horizontalWidget_3)
        self.verticalWidget_3.setObjectName(u"verticalWidget_3")
        sizePolicy2.setHeightForWidth(self.verticalWidget_3.sizePolicy().hasHeightForWidth())
        self.verticalWidget_3.setSizePolicy(sizePolicy2)
        self.verticalWidget_3.setMinimumSize(QSize(50, 0))
        self.verticalLayout_3 = QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.verticalWidget_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 24))
        self.pushButton_3.setStyleSheet(u"border:1px solid black;\n"
"background-color: rgb(139, 186, 231);")

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.lineEdit_3 = QLineEdit(self.verticalWidget_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 24))
        self.lineEdit_3.setStyleSheet(u"border:1px solid black")
        self.lineEdit_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lineEdit_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.horizontalLayout_3.addWidget(self.verticalWidget_3)

        self.plainTextEdit_3 = QPlainTextEdit(self.horizontalWidget_3)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setStyleSheet(u"border:1px solid black")

        self.horizontalLayout_3.addWidget(self.plainTextEdit_3)


        self.verticalLayout_28.addWidget(self.horizontalWidget_3)

        self.horizontalWidget_21 = QWidget(self.v_layout)
        self.horizontalWidget_21.setObjectName(u"horizontalWidget_21")
        self.horizontalLayout_26 = QHBoxLayout(self.horizontalWidget_21)
        self.horizontalLayout_26.setSpacing(5)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget_24 = QWidget(self.horizontalWidget_21)
        self.verticalWidget_24.setObjectName(u"verticalWidget_24")
        sizePolicy2.setHeightForWidth(self.verticalWidget_24.sizePolicy().hasHeightForWidth())
        self.verticalWidget_24.setSizePolicy(sizePolicy2)
        self.verticalWidget_24.setMinimumSize(QSize(50, 0))
        self.verticalLayout_27 = QVBoxLayout(self.verticalWidget_24)
        self.verticalLayout_27.setSpacing(5)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.pushButton_26 = QPushButton(self.verticalWidget_24)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setMinimumSize(QSize(0, 24))
        self.pushButton_26.setStyleSheet(u"border:1px solid black;\n"
"background-color: rgb(139, 186, 231);")

        self.verticalLayout_27.addWidget(self.pushButton_26)

        self.lineEdit_24 = QLineEdit(self.verticalWidget_24)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setMinimumSize(QSize(0, 24))
        self.lineEdit_24.setStyleSheet(u"border:1px solid black")
        self.lineEdit_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.lineEdit_24)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_24)


        self.horizontalLayout_26.addWidget(self.verticalWidget_24)

        self.plainTextEdit_24 = QPlainTextEdit(self.horizontalWidget_21)
        self.plainTextEdit_24.setObjectName(u"plainTextEdit_24")
        self.plainTextEdit_24.setStyleSheet(u"border:1px solid black")

        self.horizontalLayout_26.addWidget(self.plainTextEdit_24)


        self.verticalLayout_28.addWidget(self.horizontalWidget_21)

        self.horizontalWidget_15 = QWidget(self.v_layout)
        self.horizontalWidget_15.setObjectName(u"horizontalWidget_15")
        self.horizontalLayout_18 = QHBoxLayout(self.horizontalWidget_15)
        self.horizontalLayout_18.setSpacing(5)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget_16 = QWidget(self.horizontalWidget_15)
        self.verticalWidget_16.setObjectName(u"verticalWidget_16")
        sizePolicy2.setHeightForWidth(self.verticalWidget_16.sizePolicy().hasHeightForWidth())
        self.verticalWidget_16.setSizePolicy(sizePolicy2)
        self.verticalWidget_16.setMinimumSize(QSize(50, 0))
        self.verticalLayout_19 = QVBoxLayout(self.verticalWidget_16)
        self.verticalLayout_19.setSpacing(10)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.pushButton_18 = QPushButton(self.verticalWidget_16)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(0, 24))
        self.pushButton_18.setStyleSheet(u"border:1px solid black;\n"
"background-color: rgb(139, 186, 231);")

        self.verticalLayout_19.addWidget(self.pushButton_18)

        self.lineEdit_16 = QLineEdit(self.verticalWidget_16)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setMinimumSize(QSize(0, 24))
        self.lineEdit_16.setStyleSheet(u"border:1px solid black")
        self.lineEdit_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.lineEdit_16)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_16)


        self.horizontalLayout_18.addWidget(self.verticalWidget_16)

        self.plainTextEdit_16 = QPlainTextEdit(self.horizontalWidget_15)
        self.plainTextEdit_16.setObjectName(u"plainTextEdit_16")
        self.plainTextEdit_16.setStyleSheet(u"border:1px solid black")

        self.horizontalLayout_18.addWidget(self.plainTextEdit_16)


        self.verticalLayout_28.addWidget(self.horizontalWidget_15)

        self.horizontalWidget_5 = QWidget(self.v_layout)
        self.horizontalWidget_5.setObjectName(u"horizontalWidget_5")
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalWidget_5)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget_5 = QWidget(self.horizontalWidget_5)
        self.verticalWidget_5.setObjectName(u"verticalWidget_5")
        sizePolicy2.setHeightForWidth(self.verticalWidget_5.sizePolicy().hasHeightForWidth())
        self.verticalWidget_5.setSizePolicy(sizePolicy2)
        self.verticalWidget_5.setMinimumSize(QSize(50, 0))
        self.verticalLayout_6 = QVBoxLayout(self.verticalWidget_5)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.verticalWidget_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 24))
        self.pushButton_5.setStyleSheet(u"border:1px solid black;\n"
"background-color: rgb(139, 186, 231);")

        self.verticalLayout_6.addWidget(self.pushButton_5)

        self.lineEdit_5 = QLineEdit(self.verticalWidget_5)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(0, 24))
        self.lineEdit_5.setStyleSheet(u"border:1px solid black")
        self.lineEdit_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.lineEdit_5)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)


        self.horizontalLayout_5.addWidget(self.verticalWidget_5)

        self.plainTextEdit_5 = QPlainTextEdit(self.horizontalWidget_5)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")
        self.plainTextEdit_5.setStyleSheet(u"border:1px solid black")

        self.horizontalLayout_5.addWidget(self.plainTextEdit_5)


        self.verticalLayout_28.addWidget(self.horizontalWidget_5)

        self.horizontalWidget_6 = QWidget(self.v_layout)
        self.horizontalWidget_6.setObjectName(u"horizontalWidget_6")
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalWidget_6)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget_6 = QWidget(self.horizontalWidget_6)
        self.verticalWidget_6.setObjectName(u"verticalWidget_6")
        sizePolicy2.setHeightForWidth(self.verticalWidget_6.sizePolicy().hasHeightForWidth())
        self.verticalWidget_6.setSizePolicy(sizePolicy2)
        self.verticalWidget_6.setMinimumSize(QSize(50, 0))
        self.verticalLayout_7 = QVBoxLayout(self.verticalWidget_6)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.verticalWidget_6)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 24))
        self.pushButton_6.setStyleSheet(u"border:1px solid black;\n"
"background-color: rgb(139, 186, 231);")

        self.verticalLayout_7.addWidget(self.pushButton_6)

        self.lineEdit_6 = QLineEdit(self.verticalWidget_6)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 24))
        self.lineEdit_6.setStyleSheet(u"border:1px solid black")
        self.lineEdit_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.lineEdit_6)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_6)


        self.horizontalLayout_6.addWidget(self.verticalWidget_6)

        self.plainTextEdit_6 = QPlainTextEdit(self.horizontalWidget_6)
        self.plainTextEdit_6.setObjectName(u"plainTextEdit_6")
        self.plainTextEdit_6.setStyleSheet(u"border:1px solid black")

        self.horizontalLayout_6.addWidget(self.plainTextEdit_6)


        self.verticalLayout_28.addWidget(self.horizontalWidget_6)

        self.horizontalWidget_7 = QWidget(self.v_layout)
        self.horizontalWidget_7.setObjectName(u"horizontalWidget_7")
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalWidget_7)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget_7 = QWidget(self.horizontalWidget_7)
        self.verticalWidget_7.setObjectName(u"verticalWidget_7")
        sizePolicy2.setHeightForWidth(self.verticalWidget_7.sizePolicy().hasHeightForWidth())
        self.verticalWidget_7.setSizePolicy(sizePolicy2)
        self.verticalWidget_7.setMinimumSize(QSize(50, 0))
        self.verticalLayout_8 = QVBoxLayout(self.verticalWidget_7)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_8 = QPushButton(self.verticalWidget_7)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 24))
        self.pushButton_8.setStyleSheet(u"border:1px solid black;\n"
"background-color: rgb(139, 186, 231);")

        self.verticalLayout_8.addWidget(self.pushButton_8)

        self.lineEdit_7 = QLineEdit(self.verticalWidget_7)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(0, 24))
        self.lineEdit_7.setStyleSheet(u"border:1px solid black")
        self.lineEdit_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.lineEdit_7)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_7)


        self.horizontalLayout_8.addWidget(self.verticalWidget_7)

        self.plainTextEdit_7 = QPlainTextEdit(self.horizontalWidget_7)
        self.plainTextEdit_7.setObjectName(u"plainTextEdit_7")
        self.plainTextEdit_7.setStyleSheet(u"border:1px solid black")

        self.horizontalLayout_8.addWidget(self.plainTextEdit_7)


        self.verticalLayout_28.addWidget(self.horizontalWidget_7)

        self.horizontalWidget_4 = QWidget(self.v_layout)
        self.horizontalWidget_4.setObjectName(u"horizontalWidget_4")
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalWidget_4)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget_4 = QWidget(self.horizontalWidget_4)
        self.verticalWidget_4.setObjectName(u"verticalWidget_4")
        sizePolicy2.setHeightForWidth(self.verticalWidget_4.sizePolicy().hasHeightForWidth())
        self.verticalWidget_4.setSizePolicy(sizePolicy2)
        self.verticalWidget_4.setMinimumSize(QSize(50, 0))
        self.verticalLayout_4 = QVBoxLayout(self.verticalWidget_4)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.verticalWidget_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 24))
        self.pushButton_4.setStyleSheet(u"border:1px solid black;\n"
"background-color: rgb(139, 186, 231);")

        self.verticalLayout_4.addWidget(self.pushButton_4)

        self.lineEdit_4 = QLineEdit(self.verticalWidget_4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 24))
        self.lineEdit_4.setStyleSheet(u"border:1px solid black")
        self.lineEdit_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lineEdit_4)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)


        self.horizontalLayout_4.addWidget(self.verticalWidget_4)

        self.plainTextEdit_4 = QPlainTextEdit(self.horizontalWidget_4)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setStyleSheet(u"border:1px solid black")

        self.horizontalLayout_4.addWidget(self.plainTextEdit_4)


        self.verticalLayout_28.addWidget(self.horizontalWidget_4)

        self.splitter.addWidget(self.v_layout)
        self.cmd_layout = QWidget(self.splitter)
        self.cmd_layout.setObjectName(u"cmd_layout")
        self.verticalLayout_9 = QVBoxLayout(self.cmd_layout)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.console = QTextEdit(self.cmd_layout)
        self.console.setObjectName(u"console")
        self.console.setStyleSheet(u"border:1px solid black")

        self.verticalLayout_9.addWidget(self.console)

        self.cmd_input_layout = QWidget(self.cmd_layout)
        self.cmd_input_layout.setObjectName(u"cmd_input_layout")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cmd_input_layout.sizePolicy().hasHeightForWidth())
        self.cmd_input_layout.setSizePolicy(sizePolicy3)
        self.cmd_input_layout.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_7 = QHBoxLayout(self.cmd_input_layout)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.command_text = QPlainTextEdit(self.cmd_input_layout)
        self.command_text.setObjectName(u"command_text")
        self.command_text.setStyleSheet(u"border:1px solid black")

        self.horizontalLayout_7.addWidget(self.command_text)

        self.pushButton_7 = QPushButton(self.cmd_input_layout)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy2.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy2)
        self.pushButton_7.setMinimumSize(QSize(50, 24))
        self.pushButton_7.setStyleSheet(u"border:1px solid black")

        self.horizontalLayout_7.addWidget(self.pushButton_7)


        self.verticalLayout_9.addWidget(self.cmd_input_layout)

        self.splitter.addWidget(self.cmd_layout)

        self.verticalLayout_10.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
    # retranslateUi

