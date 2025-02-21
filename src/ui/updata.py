# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'updata.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QProgressBar, QSizePolicy, QWidget)
import static.login_icon.static_rc

class Ui_UpData(object):
    def setupUi(self, UpData):
        if not UpData.objectName():
            UpData.setObjectName(u"UpData")
        UpData.resize(690, 401)
        self.centralwidget = QWidget(UpData)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 671, 381))
        self.frame.setStyleSheet(u"\n"
"background-color:rgb(255,255,255);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 81, 41))
        font = QFont()
        font.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 M"])
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(158, 158, 158);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.jindutiao = QProgressBar(self.frame)
        self.jindutiao.setObjectName(u"jindutiao")
        self.jindutiao.setGeometry(QRect(40, 230, 601, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.jindutiao.setFont(font1)
        self.jindutiao.setStyleSheet(u"")
        self.jindutiao.setValue(0)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 80, 91, 81))
        self.label_2.setStyleSheet(u"image: url(:/login/logo.png);")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(280, 180, 91, 21))
        font2 = QFont()
        font2.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 M"])
        font2.setPointSize(10)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        UpData.setCentralWidget(self.centralwidget)

        self.retranslateUi(UpData)

        QMetaObject.connectSlotsByName(UpData)
    # setupUi

    def retranslateUi(self, UpData):
        UpData.setWindowTitle(QCoreApplication.translate("UpData", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("UpData", u"\u65b0\u7248\u672c", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("UpData", u"\u6b63\u5728\u5347\u7ea7", None))
    # retranslateUi

