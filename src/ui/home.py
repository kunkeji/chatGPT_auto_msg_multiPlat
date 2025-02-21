# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QListView, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)
import static.login_icon.static_rc
import static.icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(499, 889)
        MainWindow.setStyleSheet(u".QPushButton{\n"
"background:none;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.home = QFrame(self.centralwidget)
        self.home.setObjectName(u"home")
        self.home.setGeometry(QRect(10, 10, 481, 870))
        self.home.setStyleSheet(u"border:none;")
        self.home.setFrameShape(QFrame.Shape.StyledPanel)
        self.home.setFrameShadow(QFrame.Shadow.Raised)
        self.home.setLineWidth(0)
        self.home_right = QFrame(self.home)
        self.home_right.setObjectName(u"home_right")
        self.home_right.setGeometry(QRect(70, 0, 410, 868))
        self.home_right.setToolTipDuration(0)
        self.home_right.setStyleSheet(u"border:none;\n"
"background-color: rgb(248, 248, 248);")
        self.home_right.setFrameShape(QFrame.Shape.StyledPanel)
        self.home_right.setFrameShadow(QFrame.Shadow.Raised)
        self.home_right_top = QFrame(self.home_right)
        self.home_right_top.setObjectName(u"home_right_top")
        self.home_right_top.setGeometry(QRect(0, 0, 410, 40))
        self.home_right_top.setStyleSheet(u"background-color:rgb(255, 255, 255);")
        self.home_right_top.setFrameShape(QFrame.Shape.StyledPanel)
        self.home_right_top.setFrameShadow(QFrame.Shadow.Raised)
        self.home_top_title = QLabel(self.home_right_top)
        self.home_top_title.setObjectName(u"home_top_title")
        self.home_top_title.setEnabled(True)
        self.home_top_title.setGeometry(QRect(120, 10, 140, 22))
        font = QFont()
        font.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 M"])
        self.home_top_title.setFont(font)
        self.home_top_title.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.home_top_title.setMouseTracking(True)
        self.home_top_title.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.home_top_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top_right = QFrame(self.home_right_top)
        self.top_right.setObjectName(u"top_right")
        self.top_right.setGeometry(QRect(339, 0, 65, 40))
        self.top_right.setMinimumSize(QSize(60, 0))
        self.top_right.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.top_right.setFrameShape(QFrame.Shape.StyledPanel)
        self.top_right.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_right)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mini_but = QPushButton(self.top_right)
        self.mini_but.setObjectName(u"mini_but")
        self.mini_but.setMinimumSize(QSize(26, 26))
        self.mini_but.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.mini_but.setStyleSheet(u"#mini_but{\n"
"background-color: rgba(255, 255, 255,0);\n"
"	image: url(:/icon/icon/\u7f29\u5c0f.png);\n"
"}\n"
"\n"
"#mini_but:hover{\n"
"padding-bottom:3px\n"
"}")

        self.horizontalLayout_2.addWidget(self.mini_but)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.close_but = QPushButton(self.top_right)
        self.close_but.setObjectName(u"close_but")
        self.close_but.setMinimumSize(QSize(26, 26))
        self.close_but.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.close_but.setStyleSheet(u"#close_but{\n"
"image:url(:/icon/icon/\u5173\u95ed.png);\n"
"background-color: rgba(255, 255, 255,0);\n"
"}\n"
"#close_but:hover{\n"
"padding-bottom:3px\n"
"}")

        self.horizontalLayout_2.addWidget(self.close_but)

        self.stackedWidget = QStackedWidget(self.home_right)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QRect(0, 40, 411, 831))
        self.stackedWidget.setMinimumSize(QSize(0, 714))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 410, 828))
        self.frame_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.frame_2.setStyleSheet(u"*{\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.tableWidget = QTableWidget(self.frame_2)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ToolsCheckSpelling))
        font1 = QFont()
        font1.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 R"])
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        __qtablewidgetitem.setBackground(QColor(128, 130, 133));
        __qtablewidgetitem.setIcon(icon);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MailMessageNew))
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        __qtablewidgetitem1.setIcon(icon1);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 240, 390, 491))
        self.tableWidget.setMinimumSize(QSize(390, 432))
        self.tableWidget.setMaximumSize(QSize(390, 800))
        self.tableWidget.setFont(font1)
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(190)
        self.tableWidget.verticalHeader().setVisible(False)
        self.textEdit = QTextEdit(self.frame_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 40, 390, 190))
        self.textEdit.setMinimumSize(QSize(390, 190))
        self.textEdit.setMaximumSize(QSize(390, 180))
        self.textEdit.setFont(font1)
        self.textEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;")
        self.textEdit.setReadOnly(True)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 775, 410, 55))
        self.frame_3.setStyleSheet(u"background: rgb(237, 240, 249);")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.horizontalLayout.addWidget(self.label_2)

        self.new_key_edit = QLineEdit(self.frame_3)
        self.new_key_edit.setObjectName(u"new_key_edit")
        self.new_key_edit.setMinimumSize(QSize(72, 32))
        self.new_key_edit.setMaximumSize(QSize(72, 32))
        self.new_key_edit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.new_key_edit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.horizontalLayout.addWidget(self.label_8)

        self.new_value_edit = QLineEdit(self.frame_3)
        self.new_value_edit.setObjectName(u"new_value_edit")
        self.new_value_edit.setMinimumSize(QSize(170, 32))
        self.new_value_edit.setMaximumSize(QSize(170, 32))
        self.new_value_edit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.new_value_edit)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.pushKeyword = QPushButton(self.frame_3)
        self.pushKeyword.setObjectName(u"pushKeyword")
        self.pushKeyword.setMinimumSize(QSize(62, 32))
        self.pushKeyword.setMaximumSize(QSize(62, 32))
        self.pushKeyword.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushKeyword.setStyleSheet(u"color:#ffffff;\n"
"border-radius: 4px;\n"
"background: rgb(255, 104, 52);")

        self.horizontalLayout.addWidget(self.pushKeyword)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 410, 38))
        self.frame.setMaximumSize(QSize(16777215, 40))
        font2 = QFont()
        font2.setFamilies([u"\u4eff\u5b8b"])
        self.frame.setFont(font2)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(98, 0))
        self.label_6.setMaximumSize(QSize(98, 16777215))
        self.label_6.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.qianniu_state = QLabel(self.frame)
        self.qianniu_state.setObjectName(u"qianniu_state")
        self.qianniu_state.setMinimumSize(QSize(50, 0))
        self.qianniu_state.setMaximumSize(QSize(16777215, 40))
        font3 = QFont()
        font3.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 B"])
        font3.setBold(False)
        self.qianniu_state.setFont(font3)

        self.horizontalLayout_4.addWidget(self.qianniu_state)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setMinimumSize(QSize(60, 24))
        self.pushButton_2.setMaximumSize(QSize(60, 24))
        self.pushButton_2.setStyleSheet(u"width: 60px;\n"
"height: 24px;\n"
"box-sizing: border-box;\n"
"border: 1px solid rgba(151, 151, 151, 0.28);\n"
"border-radius: 2px;\n"
"background: rgb(0, 116, 253);\n"
"color:#fff")

        self.horizontalLayout_4.addWidget(self.pushButton_2)

        self.pipeidu = QSlider(self.frame_2)
        self.pipeidu.setObjectName(u"pipeidu")
        self.pipeidu.setGeometry(QRect(130, 745, 251, 22))
        self.pipeidu.setMinimum(1)
        self.pipeidu.setMaximum(100)
        self.pipeidu.setValue(1)
        self.pipeidu.setOrientation(Qt.Orientation.Horizontal)
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 745, 81, 22))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.frame_9 = QFrame(self.page_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(0, 780, 410, 50))
        self.frame_9.setStyleSheet(u"background: rgb(237, 240, 249);")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_18 = QLabel(self.frame_9)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_18)

        self.minganci = QLineEdit(self.frame_9)
        self.minganci.setObjectName(u"minganci")
        self.minganci.setMaximumSize(QSize(72, 32))
        self.minganci.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.minganci)

        self.label_19 = QLabel(self.frame_9)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(35, 25))
        self.label_19.setMaximumSize(QSize(35, 25))
        self.label_19.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_19)

        self.tihuan = QLineEdit(self.frame_9)
        self.tihuan.setObjectName(u"tihuan")
        self.tihuan.setMaximumSize(QSize(170, 32))
        self.tihuan.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.tihuan)

        self.mgctianjia = QPushButton(self.frame_9)
        self.mgctianjia.setObjectName(u"mgctianjia")
        self.mgctianjia.setMinimumSize(QSize(62, 32))
        self.mgctianjia.setMaximumSize(QSize(35, 25))
        self.mgctianjia.setFont(font1)
        self.mgctianjia.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.mgctianjia.setStyleSheet(u"color:#ffffff;\n"
"border-radius: 4px;\n"
"background: rgb(255, 104, 52);")

        self.horizontalLayout_3.addWidget(self.mgctianjia)

        self.minganciTable = QTableWidget(self.page_2)
        if (self.minganciTable.columnCount() < 2):
            self.minganciTable.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        __qtablewidgetitem2.setIcon(icon);
        self.minganciTable.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        __qtablewidgetitem3.setIcon(icon1);
        self.minganciTable.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.minganciTable.setObjectName(u"minganciTable")
        self.minganciTable.setGeometry(QRect(10, 10, 391, 761))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minganciTable.sizePolicy().hasHeightForWidth())
        self.minganciTable.setSizePolicy(sizePolicy)
        self.minganciTable.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;")
        self.minganciTable.setColumnCount(2)
        self.minganciTable.horizontalHeader().setDefaultSectionSize(190)
        self.minganciTable.verticalHeader().setVisible(False)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.newgoodsBut = QPushButton(self.page_3)
        self.newgoodsBut.setObjectName(u"newgoodsBut")
        self.newgoodsBut.setGeometry(QRect(300, 780, 101, 40))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.newgoodsBut.sizePolicy().hasHeightForWidth())
        self.newgoodsBut.setSizePolicy(sizePolicy1)
        self.newgoodsBut.setMinimumSize(QSize(0, 40))
        self.newgoodsBut.setFont(font1)
        self.newgoodsBut.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.newgoodsBut.setStyleSheet(u"#newgoodsBut{\n"
"color:#ffffff;\n"
"border-radius: 4px;\n"
"background: rgb(255, 104, 52);\n"
"}\n"
"")
        self.refresh = QPushButton(self.page_3)
        self.refresh.setObjectName(u"refresh")
        self.refresh.setGeometry(QRect(10, 780, 61, 41))
        self.refresh.setFont(font1)
        self.refresh.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRefresh))
        self.refresh.setIcon(icon2)
        self.refresh.setIconSize(QSize(13, 13))
        self.tabWidget = QTabWidget(self.page_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 391, 761))
        self.tabWidget.setFont(font1)
        self.tabWidget.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.listView = QListView(self.tab)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(0, 0, 391, 741))
        self.listView.setStyleSheet(u"QListView {\n"
"	font: 9pt \"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 R\";\n"
"    background-color: #ffffff; /* \u8bbe\u7f6eQListView\u7684\u80cc\u666f\u8272\u4e3a\u767d\u8272 */\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QListView::item {\n"
"    height: 30px; /* \u8bbe\u7f6e\u5217\u8868\u9879\u7684\u9ad8\u5ea6 */\n"
"    background-color: #f0f0f0; /* \u8bbe\u7f6e\u5217\u8868\u9879\u7684\u80cc\u666f\u8272 */\n"
"	border-bottom:1px solid #e3e3e3;\n"
"    border-left:3px solid rgb(233,233,233);\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background-color: #e0e0e0; /* \u8bbe\u7f6e\u5217\u8868\u9879\u60ac\u6d6e\u65f6\u7684\u80cc\u666f\u8272 */\n"
"    border-left:3px solid rgb(0, 243, 223);\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    background-color: #c0c0c0; /* \u8bbe\u7f6e\u5217\u8868\u9879\u9009\u4e2d\u65f6\u7684\u80cc\u666f\u8272 */\n"
"    color: black; /* \u8bbe\u7f6e\u9009\u4e2d\u9879\u7684\u6587\u672c\u989c\u8272 */\n"
"	border-left:3px solid rgb(247, 0, 78);\n"
"}\n"
"QScrollBar:horizontal {\n"
""
                        "    border: 1px solid #999999;\n"
"    background: #e8e8e8;\n"
"    height: 15px;\n"
"    margin: 0px 20px 0 20px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: 1px solid #999999;\n"
"    background: #e8e8e8;\n"
"    width: 15px;\n"
"    margin: 20px 0 20px 0;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #c2c2c2;\n"
"    border: 1px solid #999999;\n"
"    border-radius: 3px;\n"
"    min-width: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #c2c2c2;\n"
"    border: 1px solid #999999;\n"
"    border-radius: 3px;\n"
"    min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal,\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal,\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::do"
                        "wn-arrow:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    background-color: #333;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    border: none;\n"
"    background: none;\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    background-color: #333;\n"
"}\n"
"")
        self.listView.setMovement(QListView.Movement.Static)
        self.listView.setResizeMode(QListView.ResizeMode.Fixed)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.listView2 = QListView(self.tab_2)
        self.listView2.setObjectName(u"listView2")
        self.listView2.setGeometry(QRect(0, 0, 391, 741))
        self.listView2.setStyleSheet(u"QListView {\n"
"	font: 9pt \"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 R\";\n"
"    background-color: #ffffff; /* \u8bbe\u7f6eQListView\u7684\u80cc\u666f\u8272\u4e3a\u767d\u8272 */\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QListView::item {\n"
"    height: 30px; /* \u8bbe\u7f6e\u5217\u8868\u9879\u7684\u9ad8\u5ea6 */\n"
"    background-color: #f0f0f0; /* \u8bbe\u7f6e\u5217\u8868\u9879\u7684\u80cc\u666f\u8272 */\n"
"	border-bottom:1px solid #e3e3e3;\n"
"    border-left:3px solid rgb(233,233,233);\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background-color: #e0e0e0; /* \u8bbe\u7f6e\u5217\u8868\u9879\u60ac\u6d6e\u65f6\u7684\u80cc\u666f\u8272 */\n"
"    border-left:3px solid rgb(0, 243, 223);\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    background-color: #c0c0c0; /* \u8bbe\u7f6e\u5217\u8868\u9879\u9009\u4e2d\u65f6\u7684\u80cc\u666f\u8272 */\n"
"    color: black; /* \u8bbe\u7f6e\u9009\u4e2d\u9879\u7684\u6587\u672c\u989c\u8272 */\n"
"	border-left:3px solid rgb(247, 0, 78);\n"
"}\n"
"QScrollBar:horizontal {\n"
""
                        "    border: 1px solid #999999;\n"
"    background: #e8e8e8;\n"
"    height: 15px;\n"
"    margin: 0px 20px 0 20px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: 1px solid #999999;\n"
"    background: #e8e8e8;\n"
"    width: 15px;\n"
"    margin: 20px 0 20px 0;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #c2c2c2;\n"
"    border: 1px solid #999999;\n"
"    border-radius: 3px;\n"
"    min-width: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #c2c2c2;\n"
"    border: 1px solid #999999;\n"
"    border-radius: 3px;\n"
"    min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal,\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal,\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::do"
                        "wn-arrow:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    background-color: #333;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    border: none;\n"
"    background: none;\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    background-color: #333;\n"
"}\n"
"")
        self.tabWidget.addTab(self.tab_2, "")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.page_4)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 10, -1, -1)
        self.frame_6 = QFrame(self.page_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"font:\"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 R\";")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 0, 84, 26))
        font4 = QFont()
        font4.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 M"])
        font4.setPointSize(15)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setHintingPreference(QFont.PreferDefaultHinting)
        self.label.setFont(font4)
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(0, 760, 411, 58))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.updataBut = QPushButton(self.frame_8)
        self.updataBut.setObjectName(u"updataBut")
        sizePolicy1.setHeightForWidth(self.updataBut.sizePolicy().hasHeightForWidth())
        self.updataBut.setSizePolicy(sizePolicy1)
        self.updataBut.setMinimumSize(QSize(0, 40))
        font5 = QFont()
        font5.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 B"])
        font5.setPointSize(11)
        font5.setBold(False)
        font5.setItalic(False)
        self.updataBut.setFont(font5)
        self.updataBut.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.updataBut.setStyleSheet(u"#updataBut{\n"
"background-color: rgb(255, 104, 52);\n"
"border-radius: 7px;\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_8.addWidget(self.updataBut)

        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(40, 66, 101, 16))
        font6 = QFont()
        font6.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 M"])
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setItalic(False)
        self.label_10.setFont(font6)
        self.tishici = QTextEdit(self.frame_6)
        self.tishici.setObjectName(u"tishici")
        self.tishici.setGeometry(QRect(10, 90, 391, 201))
        self.tishici.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;")
        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(37, 306, 91, 16))
        self.label_12.setFont(font6)
        self.tishici2 = QTextEdit(self.frame_6)
        self.tishici2.setObjectName(u"tishici2")
        self.tishici2.setGeometry(QRect(10, 330, 391, 181))
        self.tishici2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;")
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 3, 25, 24))
        self.label_3.setMinimumSize(QSize(24, 24))
        self.label_3.setStyleSheet(u"image: url(:/login/imshezhi.png);")
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 64, 21, 21))
        self.label_4.setStyleSheet(u"image: url(:/login/rengongzhineng.png);")
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 304, 21, 21))
        self.label_5.setStyleSheet(u"image: url(:/login/tongyong.png);")

        self.horizontalLayout_9.addWidget(self.frame_6)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.cloerBut = QPushButton(self.page_5)
        self.cloerBut.setObjectName(u"cloerBut")
        self.cloerBut.setGeometry(QRect(100, 520, 201, 41))
        self.cloerBut.setMinimumSize(QSize(0, 41))
        self.cloerBut.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cloerBut.setStyleSheet(u"#cloerBut{\n"
"background-color:rgb(255, 104, 52);\n"
"border-radius: 7px;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.frame_5 = QFrame(self.page_5)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(160, 70, 80, 80))
        self.frame_5.setStyleSheet(u"border-radius: 40px;\n"
"border:5px solid rgb(255, 255, 255);\n"
"padding:3px;\n"
"image: url(:/login/logo.png);\n"
"")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.modify = QPushButton(self.page_5)
        self.modify.setObjectName(u"modify")
        self.modify.setGeometry(QRect(100, 440, 201, 41))
        self.modify.setMinimumSize(QSize(0, 41))
        self.modify.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.modify.setStyleSheet(u"#modify{\n"
"background-color: rgb(255, 104, 52);\n"
"border-radius: 7px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.layoutWidget = QWidget(self.page_5)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(100, 200, 201, 191))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)

        self.username = QLabel(self.layoutWidget)
        self.username.setObjectName(u"username")
        self.username.setFont(font)

        self.gridLayout.addWidget(self.username, 0, 1, 1, 1)

        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_11, 1, 0, 1, 1)

        self.emall = QLabel(self.layoutWidget)
        self.emall.setObjectName(u"emall")

        self.gridLayout.addWidget(self.emall, 1, 1, 1, 1)

        self.label_14 = QLabel(self.layoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_14, 2, 0, 1, 1)

        self.birthday = QLabel(self.layoutWidget)
        self.birthday.setObjectName(u"birthday")
        self.birthday.setFont(font)

        self.gridLayout.addWidget(self.birthday, 2, 1, 1, 1)

        self.label_16 = QLabel(self.layoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_16, 3, 0, 1, 1)

        self.phone = QLabel(self.layoutWidget)
        self.phone.setObjectName(u"phone")
        self.phone.setFont(font)

        self.gridLayout.addWidget(self.phone, 3, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_5)
        self.home_left = QFrame(self.home)
        self.home_left.setObjectName(u"home_left")
        self.home_left.setGeometry(QRect(0, 0, 72, 870))
        self.home_left.setMinimumSize(QSize(72, 870))
        self.home_left.setStyleSheet(u"background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 rgb(0, 177, 255), stop: 1.0158 rgb(0, 116, 253));\n"
"border:none")
        self.home_left.setFrameShape(QFrame.Shape.StyledPanel)
        self.home_left.setFrameShadow(QFrame.Shadow.Raised)
        self.home_left.setLineWidth(0)
        self.about = QPushButton(self.home_left)
        self.about.setObjectName(u"about")
        self.about.setGeometry(QRect(27, 827, 20, 20))
        self.about.setStyleSheet(u"image: url(:/icon/icon/\u7591\u95ee.png);")
        self.munu = QFrame(self.home_left)
        self.munu.setObjectName(u"munu")
        self.munu.setGeometry(QRect(7, 110, 58, 311))
        self.munu.setStyleSheet(u"QPushButton:hover {\n"
"	background-image: url(:/icon/icon/\u9009\u4e2d\u5706.png);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.munu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.home_but = QPushButton(self.munu)
        self.home_but.setObjectName(u"home_but")
        self.home_but.setMinimumSize(QSize(40, 40))
        self.home_but.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.home_but.setStyleSheet(u"image: url(:/icon/icon/\u9996\u9875.png);")

        self.verticalLayout_2.addWidget(self.home_but)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.keyword_but = QPushButton(self.munu)
        self.keyword_but.setObjectName(u"keyword_but")
        self.keyword_but.setMinimumSize(QSize(40, 40))
        self.keyword_but.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.keyword_but.setStyleSheet(u"image:url(:/icon/icon/minganci.png)")

        self.verticalLayout_2.addWidget(self.keyword_but)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.massg_but = QPushButton(self.munu)
        self.massg_but.setObjectName(u"massg_but")
        self.massg_but.setMinimumSize(QSize(40, 40))
        self.massg_but.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.massg_but.setStyleSheet(u"image: url(:/icon/icon/\u654f\u611f\u8bcd.png)")

        self.verticalLayout_2.addWidget(self.massg_but)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.setup_but = QPushButton(self.munu)
        self.setup_but.setObjectName(u"setup_but")
        self.setup_but.setMinimumSize(QSize(40, 40))
        self.setup_but.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setup_but.setStyleSheet(u"image: url(:/icon/icon/\u8bbe\u7f6e.png)")

        self.verticalLayout_2.addWidget(self.setup_but)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.my_but = QPushButton(self.munu)
        self.my_but.setObjectName(u"my_but")
        self.my_but.setMinimumSize(QSize(40, 40))
        self.my_but.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.my_but.setStyleSheet(u"image:url(:/icon/icon/\u6211\u7684.png)")

        self.verticalLayout_2.addWidget(self.my_but)

        self.logo = QLabel(self.home_left)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(5, 41, 65, 47))
        self.logo.setMinimumSize(QSize(65, 47))
        self.logo.setMaximumSize(QSize(65, 16777215))
        self.logo.setStyleSheet(u"image: url(:/login/logo.png);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.close_but.clicked.connect(MainWindow.close)
        self.mini_but.clicked.connect(MainWindow.showMinimized)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.home_top_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#21252b;\">\u9996\u9875</span></p></body></html>", None))
        self.mini_but.setText("")
        self.close_but.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u5173\u952e\u8bcd", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u5185\u5bb9", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8bcd", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u5185\u5bb9", None))
        self.pushKeyword.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u5343\u725b\u72b6\u6001\uff1a", None))
        self.qianniu_state.setText(QCoreApplication.translate("MainWindow", u"\u672a\u8fde\u63a5", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5\u5343\u725b", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u5173\u952e\u8bcd\u5339\u914d\u5ea6", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u654f\u611f\u8bcd", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u66ff\u6362\u8bcd", None))
        self.mgctianjia.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        ___qtablewidgetitem2 = self.minganciTable.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u5173\u952e\u8bcd", None));
        ___qtablewidgetitem3 = self.minganciTable.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u66ff\u6362\u5185\u5bb9", None));
        self.newgoodsBut.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5546\u54c1", None))
        self.refresh.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u5df2\u5b8c\u5584", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u5f85\u5b8c\u5584", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf\u8bbe\u7f6e", None))
        self.updataBut.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u8bbe\u7f6e", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u89d2\u8272\u63cf\u8ff0", None))
        self.tishici.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u7684\u63d0\u793a\u8bcd\u7528\u4e8e\u5728\u5546\u54c1\u6709\u8bf4\u660e\u4e66\u7684\u60c5\u51b5\u4e0b\uff0cAI\u4f1a\u6309\u7167\u4f60\u7684\u63cf\u8ff0\u5145\u5f53\u89d2\u8272", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u901a\u7528\u89d2\u8272\u63cf\u8ff0", None))
        self.tishici2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u7684\u63d0\u793a\u8bcd\u7528\u4e8e\u65e0\u5546\u54c1\u8bf4\u660e\u4e66\u7684\u60c5\u51b5\u4e0b\uff0c\u5982\u679c\u5728\u6ca1\u6709\u77e5\u8bc6\u548c\u5173\u952e\u8bcd\u5339\u914d\u7684\u60c5\u51b5\u4e0b\u5e0c\u671b\u63d0\u9192\u4eba\u5de5\u63a5\u5165\uff0c\u8bf7\u5728\u6b64\u586b\u5199\u201c\u53ea\u80fd\u56de\u590d\u2018\u8bf7\u7a0d\u7b49\u2019\u201d", None))
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.cloerBut.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u767b\u5f55", None))
        self.modify.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u4e2a\u4eba\u8d44\u6599", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d\uff1a", None))
        self.username.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u90ae\u7bb1\uff1a", None))
        self.emall.setText(QCoreApplication.translate("MainWindow", u"\u90ae\u7bb1", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u751f\u65e5\uff1a", None))
        self.birthday.setText(QCoreApplication.translate("MainWindow", u"\u751f\u65e5", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u624b\u673a\u53f7\uff1a", None))
        self.phone.setText(QCoreApplication.translate("MainWindow", u"\u624b\u673a\u53f7", None))
        self.about.setText("")
        self.home_but.setText("")
        self.keyword_but.setText("")
        self.massg_but.setText("")
        self.setup_but.setText("")
        self.my_but.setText("")
        self.logo.setText("")
    # retranslateUi

