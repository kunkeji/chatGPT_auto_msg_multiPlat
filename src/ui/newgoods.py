# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newgoods.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(910, 551)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"\n"
"*{\n"
"	font: \"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 R\";\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.Title = QLabel(self.frame)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(340, 10, 261, 20))
        font = QFont()
        font.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 M"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.Title.setFont(font)
        self.Title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 60, 71, 21))
        font1 = QFont()
        font1.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 M"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.label.setFont(font1)
        self.goodsurl = QLineEdit(self.frame)
        self.goodsurl.setObjectName(u"goodsurl")
        self.goodsurl.setGeometry(QRect(100, 50, 781, 31))
        font2 = QFont()
        font2.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 M"])
        font2.setBold(False)
        font2.setItalic(False)
        self.goodsurl.setFont(font2)
        self.goodsname = QLineEdit(self.frame)
        self.goodsname.setObjectName(u"goodsname")
        self.goodsname.setGeometry(QRect(100, 90, 321, 31))
        self.goodsname.setFont(font2)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 100, 61, 21))
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(440, 100, 71, 21))
        self.label_3.setFont(font1)
        self.shopname = QLineEdit(self.frame)
        self.shopname.setObjectName(u"shopname")
        self.shopname.setGeometry(QRect(510, 90, 371, 31))
        self.shopname.setFont(font2)
        self.welcome = QTextEdit(self.frame)
        self.welcome.setObjectName(u"welcome")
        self.welcome.setGeometry(QRect(20, 180, 191, 311))
        self.welcome.setFont(font2)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 150, 111, 16))
        self.label_4.setFont(font2)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(250, 150, 111, 16))
        self.label_5.setFont(font2)
        self.instructions = QTextEdit(self.frame)
        self.instructions.setObjectName(u"instructions")
        self.instructions.setGeometry(QRect(240, 180, 651, 311))
        self.instructions.setFont(font2)
        self.close = QPushButton(self.frame)
        self.close.setObjectName(u"close")
        self.close.setGeometry(QRect(834, 10, 41, 31))
        self.close.setFont(font2)
        self.close.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.close.setStyleSheet(u"boroder:none\n"
"")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditClear))
        self.close.setIcon(icon)
        self.add = QPushButton(self.frame)
        self.add.setObjectName(u"add")
        self.add.setGeometry(QRect(804, 500, 81, 31))
        font3 = QFont()
        font3.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 B"])
        font3.setBold(False)
        font3.setItalic(False)
        self.add.setFont(font3)
        self.add.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add.setStyleSheet(u"background-color: rgb(85, 255, 0);")
        self.delgoods = QPushButton(self.frame)
        self.delgoods.setObjectName(u"delgoods")
        self.delgoods.setGeometry(QRect(20, 500, 91, 31))
        self.delgoods.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.delgoods.setStyleSheet(u"color: rgb(255,255, 255);\n"
"background-color: rgb(255, 0, 0);")

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.close.clicked.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5546\u54c1\u8bf4\u660e\u4e66", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5546\u54c1\u94fe\u63a5\uff1a", None))
        self.goodsurl.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u6dd8\u5b9d\u6216\u5929\u732b\u94fe\u63a5", None))
        self.goodsname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5546\u54c1\u540d\u79f0\u9700\u4e0e\u94fe\u63a5\u5546\u54c1\u540d\u79f0\u4e00\u81f4", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5546\u54c1\u540d\u79f0\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5e97\u94fa\u540d\u79f0\uff1a", None))
        self.welcome.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 M'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Microsoft YaHei UI';\"><br /></p></body></html>", None))
        self.welcome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"     \u5f53\u7528\u6237\u9996\u6b21\u901a\u8fc7\u672c\u5546\u54c1\u8fdb\u5165\u5ba2\u670d\u804a\u5929\u65f6\u4f1a\u81ea\u52a8\u53d1\u9001\u7ed9\u7528\u6237", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5546\u54c1\u6b22\u8fce\u8bcd\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u5546\u54c1\u8bf4\u660e\u4e66\uff1a", None))
        self.instructions.setPlaceholderText(QCoreApplication.translate("MainWindow", u"    \u5546\u54c1\u8bf4\u660e\u8bf4\u662fAI\u5bf9\u672c\u4ea7\u54c1\u8ba4\u77e5\u7684\u6765\u6e90\uff0c\u5199\u7684\u8d8a\u8be6\u7ec6AI\u80fd\u591f\u56de\u7b54\u7684\u95ee\u9898\u5c31\u8d8a\u591a\u3002\u6700\u597d\u7ed3\u5408\u4ee5\u5f80\u7684\u804a\u5929\u4fe1\u606f\u7f16\u5199\u3002", None))
        self.close.setText("")
        self.add.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5546\u54c1", None))
        self.delgoods.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u5546\u54c1", None))
    # retranslateUi

