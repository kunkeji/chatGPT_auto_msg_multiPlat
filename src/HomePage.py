import win32gui
import json
from PyQt6.QtWidgets import QMessageBox,QLineEdit,QMenu,QTableWidget, QWidget,QTableWidgetItem, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,  QCheckBox, QTextEdit
from PyQt6.QtGui import QIcon,  QCursor,QAction
from PyQt6.QtCore import Qt, QSize



from config.const import *
from config.globals import *
from ttkbootstrap.constants import *
from config.Config import Config

config = Config()
class HomePage(QWidget):
    
    global KEYWORD_FILE
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        # 创建垂直布局
        layout = QVBoxLayout(self)
        # 初始化平台复选框字典
        self.platform_checkboxes = {}
        # 创建平台容器部件
        platform_widget = QWidget()
        # 创建平台水平布局
        platform_layout = QHBoxLayout(platform_widget)
        for name in PLATFORMS:
            # 创建复选框
            checkbox = QCheckBox(name)
            # 设置复选框样式
            checkbox.setStyleSheet("font-size: 12px;")
            # 设置复选框默认不可选择
            checkbox.setEnabled(False)  # 默认不可选择
            # 连接复选框状态改变的信号
            checkbox.stateChanged.connect(lambda state, platform=name: self.update_platform_state(platform, state))
            # 将复选框添加到平台复选框字典中
            self.platform_checkboxes[name] = checkbox
            # 将复选框添加到平台布局中
            platform_layout.addWidget(checkbox)
            # 在复选框之间添加间距
            platform_layout.addSpacing(10)
        # 创建刷新按钮
        refresh_button = QPushButton()
        # 设置刷新按钮的图标
        refresh_button.setIcon(QIcon("./static/image/icons/refresh.png"))
        # 设置刷新按钮图标的大小
        refresh_button.setIconSize(QSize(25, 25))
        # 设置刷新按钮的样式
        refresh_button.setStyleSheet("font-size: 12px; background-color: transparent;")
        # 连接刷新按钮的点击信号
        refresh_button.clicked.connect(self.refresh_platform_status)
        # 将刷新按钮添加到平台布局中
        platform_layout.addWidget(refresh_button)
        # 将平台容器部件添加到主布局中
        layout.addWidget(platform_widget)
        # 日志显示
        # 创建日志显示文本框
        self.log_widget = QTextEdit()
        # 设置日志显示文本框的高度
        self.log_widget.setFixedHeight(150)
        # 设置日志显示文本框的样式
        self.log_widget.setStyleSheet("background-color: white; border: 1px solid gray;")
        # 设置日志显示文本框为只读
        self.log_widget.setReadOnly(True)
        # 将日志显示文本框添加到主布局中
        layout.addWidget(self.log_widget)
        # 设置关键词文件的路径
        self.KEYWORD_FILE = KEYWORD_FILE  # 文件路径
        # 加载关键词
        self.load_keywords()
        # 创建一个表格部件，并根据关键词数量设置行数和列数（固定为2列）
        self.keyword_table = QTableWidget(len(self.keywords), 2)
        # 设置表格的表头标签
        self.keyword_table.setHorizontalHeaderLabels(['触发词', '回复内容'])
        # 设置表格的样式表
        self.keyword_table.setStyleSheet("background-color: white; ")
        # 设置第一列的宽度为100像素
        self.keyword_table.setColumnWidth(0, 100)
        # 设置第二列的宽度为205像素
        self.keyword_table.setColumnWidth(1, 220)
        # 设置表格的垂直表头隐藏
        self.keyword_table.verticalHeader().setVisible(False)
        # 填充表格数据
        self.populate_table()
        # 设置表格的上下文菜单策略为自定义上下文菜单
        self.keyword_table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        # 连接表格的自定义上下文菜单请求信号到showContextMenu槽函数
        self.keyword_table.customContextMenuRequested.connect(self.showContextMenu)
        # 连接表格的项变化信号到item_changed槽函数
        self.keyword_table.itemChanged.connect(self.item_changed)
        # 将表格部件添加到布局中
        layout.addWidget(self.keyword_table)
        # 创建一个新的水平布局用于添加关键词和回复内容
        new_keyword_layout = QHBoxLayout()
        # 创建一个新的关键词输入框
        self.new_key_edit = QLineEdit()
        self.new_key_edit.setStyleSheet("""
            QLineEdit {
                background-color: white;
                height: 25px;
                padding-left: 5px;
                border-radius: 5px;
                border: none;
            }
        """)
        # 创建一个新的回复内容输入框
        self.new_value_edit = QLineEdit()
        self.new_value_edit.setStyleSheet("""
            QLineEdit {
                background-color: white;
                height: 25px;
                padding-left: 5px;
                border-radius: 5px;
                border: none;
            }
        """)
        # 创建一个添加按钮
        add_button = QPushButton("添加")
        # 连接添加按钮的点击信号到add_new_keyword槽函数
        add_button.clicked.connect(self.add_new_keyword)
        # 设置添加按钮的鼠标光标为手形光标
        add_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        # 设置添加按钮的样式表
        add_button.setStyleSheet("QPushButton { background-color: #343A40;color:#fff; border-radius: 4px; padding: 6px; }")
        # 向新关键词布局中添加标签和输入框
        new_keyword_layout.addWidget(QLabel("词:"))
        new_keyword_layout.addWidget(self.new_key_edit)
        new_keyword_layout.addWidget(QLabel("内容:"))
        new_keyword_layout.addWidget(self.new_value_edit)
        new_keyword_layout.addWidget(add_button)
        # 将新关键词布局添加到主布局中
        layout.addLayout(new_keyword_layout)
        # 设置窗口或部件的布局为主布局
        self.setLayout(layout)

    def load_keywords(self):
        try:
            with open(self.KEYWORD_FILE, 'r', encoding='utf-8') as file:
                self.keywords = json.load(file)
        except FileNotFoundError:
            self.keywords = {}
    
    def populate_table(self):
        self.keyword_table.setRowCount(len(self.keywords))
        row = 0
        for key, value in self.keywords.items():
            self.keyword_table.setItem(row, 0, QTableWidgetItem(key))
            self.keyword_table.setItem(row, 1, QTableWidgetItem(value))
            row += 1
    
    def showContextMenu(self, pos):
        contextMenu = QMenu(self)
        deleteAction = QAction("删除选中", self)
        deleteAction.triggered.connect(self.deleteItem)
        contextMenu.addAction(deleteAction)
        contextMenu.exec(self.keyword_table.mapToGlobal(pos))
    
    def deleteItem(self):
        current_row = self.keyword_table.currentRow()
        if current_row >= 0:
            key_item = self.keyword_table.item(current_row, 0)
            key = key_item.text()
            del self.keywords[key]
            self.keyword_table.removeRow(current_row)
            self.save_to_file()
    
    def save_to_file(self):
        with open(self.KEYWORD_FILE, 'w', encoding='utf-8') as file:
            json.dump(self.keywords, file, ensure_ascii=False, indent=4)

    def item_changed(self, item):
        if item.column() == 1:
            row = item.row()
            key_item = self.keyword_table.item(row, 0)
            value_item = self.keyword_table.item(row, 1)
            key = key_item.text()
            new_value = value_item.text()
            self.keywords[key] = new_value
            self.save_to_file()
    
    def add_new_keyword(self):
        new_key = self.new_key_edit.text().strip()
        new_value = self.new_value_edit.text().strip()
        if new_key and new_value:
            if new_key in self.keywords:
                QMessageBox.warning(self, "重复关键词", f"这个关键词'{new_key}'已经添加过了.")
            else:
                self.keywords[new_key] = new_value
                row_position = self.keyword_table.rowCount()
                self.keyword_table.insertRow(row_position)
                self.keyword_table.setItem(row_position, 0, QTableWidgetItem(new_key))
                self.keyword_table.setItem(row_position, 1, QTableWidgetItem(new_value))
                self.new_key_edit.clear()
                self.new_value_edit.clear()
                self.save_to_file()
        else:
            QMessageBox.warning(self, "缺少输入", "请输入关键词和出发内容.")
   
    def refresh_platform_status(self):
        # global PDD_SELECT, QN_SELECT, DD_SELECT,PDD_APP_HWND, QN_APP_HWND, DD_APP_HWND

        

        config.PDD_APP_HWND = win32gui.FindWindow(config.PDD_APP_CLASS_NAME, config.PDD_APP_TITLE)
        config.QN_APP_HWND = win32gui.FindWindow(config.QN_APP_CLASS_NAME, config.QN_APP_TITLE)
        config.DD_APP_HWND = win32gui.FindWindow(config.DD_APP_CLASS_NAME, config.DD_APP_TITLE)

        config.PDD_SELECT = config.PDD_APP_HWND != 0
        config.QN_SELECT = config.QN_APP_HWND != 0
        config.DD_SELECT = config.DD_APP_HWND != 0

        for name, checkbox in self.platform_checkboxes.items():
            checkbox.setEnabled(name == "千牛" and config.QN_SELECT or
                                name == "拼多多" and config.PDD_SELECT or
                                name == "抖店" and config.DD_SELECT)
            if name == "千牛" and config.QN_SELECT:
                checkbox.setChecked(True)
            elif name == "拼多多" and config.PDD_SELECT:
                checkbox.setChecked(True)
            elif name == "抖店" and config.DD_SELECT:

                checkbox.setChecked(True)
            else:
                checkbox.setChecked(False)
        self.parent.log_message("平台状态已刷新.")
    
    def update_platform_state(self, platform, state):
        if platform == "拼多多":
            config.PDD_SELECT = state if True else False
        elif platform == "千牛":
            config.QN_SELECT = state if True else False
        elif platform == "抖店":
            config.DD_SELECT = state  if True else False
    def append_log_message(self, message):
        self.log_widget.append(message)