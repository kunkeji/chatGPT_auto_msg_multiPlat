# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import static.login_icon.static_rc

class Ui_LoginPage(object):
    def setupUi(self, LoginPage):
        if not LoginPage.objectName():
            LoginPage.setObjectName(u"LoginPage")
        LoginPage.resize(450, 580)
        icon = QIcon()
        icon.addFile(u":/login/logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        LoginPage.setWindowIcon(icon)
        LoginPage.setStyleSheet(u"*{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.centralwidget = QWidget(LoginPage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainBox = QFrame(self.centralwidget)
        self.mainBox.setObjectName(u"mainBox")
        self.mainBox.setGeometry(QRect(10, 10, 431, 560))
        self.mainBox.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.mainBox.setStyleSheet(u"\n"
"#mainBox{\n"
"background-color: qlineargradient(\n"
"    spread:pad,\n"
"    x1:0, y1:0,\n"
"    x2:1, y2:1,\n"
"	stop:0 rgba(52, 58, 64, 255),\n"
"    stop:1 rgb(33, 37, 43)\n"
"    \n"
");\n"
"	background-color:rgb(33, 37, 43);\n"
"width:420px;\n"
"height:520px;\n"
"}")
        self.mainBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainBox.setFrameShadow(QFrame.Shadow.Raised)
        self.frame = QFrame(self.mainBox)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 30, 431, 120))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        self.frame.setFont(font)
        self.frame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logoBox = QFrame(self.frame)
        self.logoBox.setObjectName(u"logoBox")
        self.logoBox.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logoBox.sizePolicy().hasHeightForWidth())
        self.logoBox.setSizePolicy(sizePolicy)
        self.logoBox.setMinimumSize(QSize(100, 100))
        self.logoBox.setMaximumSize(QSize(100, 100))
        self.logoBox.setStyleSheet(u"image: url(:/login/logo.png);\n"
"")
        self.logoBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.logoBox.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.logoBox)

        self.frame_2 = QFrame(self.mainBox)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 140, 430, 60))
        self.frame_2.setMinimumSize(QSize(430, 0))
        self.frame_2.setToolTipDuration(-1)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.loginTitle = QLabel(self.frame_2)
        self.loginTitle.setObjectName(u"loginTitle")
        font1 = QFont()
        font1.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 R"])
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(False)
        self.loginTitle.setFont(font1)
        self.loginTitle.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.loginTitle, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_3 = QFrame(self.mainBox)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(90, 220, 248, 41))
        self.frame_3.setMinimumSize(QSize(248, 41))
        self.frame_3.setMaximumSize(QSize(248, 41))
        self.frame_3.setStyleSheet(u"border-radius: 4px;\n"
"background: rgb(250, 171, 34);")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(22, 22))
        self.label_2.setMaximumSize(QSize(22, 22))
        self.label_2.setStyleSheet(u"image: url(:/login/dengluzhanghao.png);")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.username = QLineEdit(self.frame_3)
        self.username.setObjectName(u"username")
        self.username.setMinimumSize(QSize(200, 35))
        self.username.setMaximumSize(QSize(210, 35))
        font2 = QFont()
        font2.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 M"])
        self.username.setFont(font2)
        self.username.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.username.setStyleSheet(u"background-color:rgb(250, 228, 101);\n"
"padding-left:5px;")

        self.horizontalLayout_3.addWidget(self.username)

        self.frame_4 = QFrame(self.mainBox)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(90, 290, 248, 41))
        self.frame_4.setMinimumSize(QSize(248, 41))
        self.frame_4.setMaximumSize(QSize(248, 41))
        self.frame_4.setStyleSheet(u"border-radius: 4px;\n"
"background: rgb(250, 171, 34);")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(22, 22))
        self.label_3.setMaximumSize(QSize(22, 22))
        self.label_3.setStyleSheet(u"\n"
"image: url(:/login/mima.png);")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.password = QLineEdit(self.frame_4)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(200, 35))
        self.password.setMaximumSize(QSize(210, 35))
        self.password.setFont(font2)
        self.password.setStyleSheet(u"background-color:rgb(250, 228, 101);\n"
"padding-left:5px;")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.setCursorPosition(0)

        self.horizontalLayout_4.addWidget(self.password)

        self.frame_5 = QFrame(self.mainBox)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(90, 340, 248, 31))
        self.frame_5.setMinimumSize(QSize(248, 0))
        self.frame_5.setMaximumSize(QSize(248, 16777215))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.frame_5)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(72, 19))
        self.checkBox.setMaximumSize(QSize(72, 19))
        self.checkBox.setFont(font2)
        self.checkBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBox.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.checkBox.setChecked(False)

        self.horizontalLayout_5.addWidget(self.checkBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.checkBox_2 = QCheckBox(self.frame_5)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setMinimumSize(QSize(72, 19))
        self.checkBox_2.setMaximumSize(QSize(72, 19))
        self.checkBox_2.setFont(font2)
        self.checkBox_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBox_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.checkBox_2)

        self.layoutWidget = QWidget(self.mainBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(350, 0, 74, 29))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.setMinbut = QPushButton(self.layoutWidget)
        self.setMinbut.setObjectName(u"setMinbut")
        self.setMinbut.setMinimumSize(QSize(0, 0))
        self.setMinbut.setMaximumSize(QSize(24, 24))
        self.setMinbut.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setMinbut.setStyleSheet(u"#setMinbut{\n"
"	image: url(:/login/zuixiaohua_1.png);\n"
"	background:rgba(0,0,0,0)\n"
"}\n"
"#setMinbut:hover{\n"
"padding-bottom:3px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.setMinbut)

        self.horizontalSpacer = QSpacerItem(13, 27, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.setColsebut = QPushButton(self.layoutWidget)
        self.setColsebut.setObjectName(u"setColsebut")
        self.setColsebut.setMinimumSize(QSize(0, 0))
        self.setColsebut.setMaximumSize(QSize(24, 24))
        self.setColsebut.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setColsebut.setStyleSheet(u"\n"
"#setColsebut{\n"
"	background-color:rgba(0,0,0,0);\n"
"	image: url(:/login/guanbi_1.png);\n"
"}\n"
"#setColsebut:hover{\n"
"	padding-bottom:3px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.setColsebut)

        self.loginBut = QPushButton(self.mainBox)
        self.loginBut.setObjectName(u"loginBut")
        self.loginBut.setGeometry(QRect(90, 420, 248, 41))
        self.loginBut.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.loginBut.setStyleSheet(u"#loginBut{\n"
"background-color: rgb(250, 173, 20);\n"
"border-radius: 7px;\n"
"border-bottom:4px solid rgb(208, 141, 16);\n"
"}\n"
"#loginBut:hover{\n"
"background-color:rgb(250, 173, 20);\n"
"border-bottom:0px solid rgb(208, 141, 16);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/login/denglu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.loginBut.setIcon(icon1)
        self.loginBut.setIconSize(QSize(40, 40))
        self.frame_6 = QFrame(self.mainBox)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(90, 470, 248, 35))
        self.frame_6.setMaximumSize(QSize(248, 16777215))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.frame_6)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(60, 30))
        self.pushButton_3.setMaximumSize(QSize(60, 30))
        self.pushButton_3.setFont(font2)
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:#ffffff")

        self.horizontalLayout_6.addWidget(self.pushButton_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.pushButton_4 = QPushButton(self.frame_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(80, 30))
        self.pushButton_4.setMaximumSize(QSize(80, 30))
        self.pushButton_4.setFont(font2)
        self.pushButton_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:#ffffff")
        icon2 = QIcon()
        icon2.addFile(u":/login/wangjimima.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QSize(28, 28))
        self.pushButton_4.setAutoDefault(False)

        self.horizontalLayout_6.addWidget(self.pushButton_4)

        self.label_4 = QLabel(self.mainBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(230, 530, 171, 20))
        font3 = QFont()
        font3.setPointSize(6)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.frame_5.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.layoutWidget.raise_()
        self.loginBut.raise_()
        self.frame_6.raise_()
        self.label_4.raise_()
        LoginPage.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.username, self.password)
        QWidget.setTabOrder(self.password, self.loginBut)
        QWidget.setTabOrder(self.loginBut, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.checkBox_2)
        QWidget.setTabOrder(self.checkBox_2, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.setMinbut)
        QWidget.setTabOrder(self.setMinbut, self.setColsebut)

        self.retranslateUi(LoginPage)
        self.setColsebut.clicked.connect(LoginPage.close)
        self.setMinbut.clicked.connect(LoginPage.showMinimized)

        QMetaObject.connectSlotsByName(LoginPage)
    # setupUi

    def retranslateUi(self, LoginPage):
        LoginPage.setWindowTitle(QCoreApplication.translate("LoginPage", u"\u58f3\u6797\u667a\u80fd\u5ba2\u670d", None))
        self.loginTitle.setText(QCoreApplication.translate("LoginPage", u"\u58f3\u6797\u667a\u80fd\u5ba2\u670d", None))
        self.label_2.setText("")
        self.username.setInputMask("")
        self.username.setPlaceholderText(QCoreApplication.translate("LoginPage", u"\u8bf7\u8f93\u5165\u8d26\u53f7", None))
        self.label_3.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("LoginPage", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.checkBox.setText(QCoreApplication.translate("LoginPage", u"\u8bb0\u4f4f\u5bc6\u7801", None))
        self.checkBox_2.setText(QCoreApplication.translate("LoginPage", u"\u81ea\u52a8\u767b\u5f55", None))
        self.setMinbut.setText("")
        self.setColsebut.setText("")
        self.loginBut.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("LoginPage", u"\u7acb\u5373\u6ce8\u518c", None))
        self.pushButton_4.setText(QCoreApplication.translate("LoginPage", u"\u5fd8\u8bb0\u5bc6\u7801", None))
        self.label_4.setText(QCoreApplication.translate("LoginPage", u"20240824.A.52.9", None))
    # retranslateUi

