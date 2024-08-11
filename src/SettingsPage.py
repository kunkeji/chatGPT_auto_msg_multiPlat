
import json

from PyQt6.QtWidgets import QSpacerItem,QSizePolicy,QMessageBox,QLineEdit,QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtGui import  QCursor
from PyQt6.QtCore import Qt

from ttkbootstrap.constants import *

from config.Config import Config

config = Config()

#设置
class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setSpacing(10)  # 设置控件之间的间距
        self.setLayout(layout)

        self.config_file = 'config/config.json'
        self.config_data = self.load_config()

        # 添加标题标签
        title_label = QLabel("设置")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")

        # 创建URL设置项
        url_label = QLabel("fastGPT_URL:", alignment=Qt.AlignmentFlag.AlignLeft)
        self.url_edit = QLineEdit(self.config_data.get('AI_URL', ''))
        self.url_edit.setStyleSheet("""
            QLineEdit {
                background-color: white;
                height: 40px;
                padding-left: 5px;
                border-radius: 5px;
                border: none;
            }
        """)

        # 创建Key设置项
        key_label = QLabel("fastGPT_Key:", alignment=Qt.AlignmentFlag.AlignLeft)
        self.key_edit = QLineEdit(self.config_data.get('AI_KEY', ''))
        self.key_edit.setStyleSheet("""
            QLineEdit {
                background-color: white;
                height: 40px;
                padding-left: 5px;
                border-radius: 5px;
                border: none;
            }
        """)

        # 创建保存按钮
        save_button = QPushButton("保存并更新")
        save_button.setFixedSize(100, 40)
        save_button.setStyleSheet("""
            QPushButton {
                background-color: white;
                height: 40px;
                border-radius: 5px;
                border: none;
            }
            QPushButton:hover {
                background-color: green;
                cursor: pointer;
            }
        """)
        save_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        save_button.clicked.connect(self.save_settings)

        # 添加控件到布局中
        layout.addWidget(title_label)
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))  # 添加空白项
        layout.addWidget(url_label)
        layout.addWidget(self.url_edit)
        layout.addWidget(key_label)
        layout.addWidget(self.key_edit)
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))  # 添加空白项
        layout.addWidget(save_button, alignment=Qt.AlignmentFlag.AlignCenter)

    def load_config(self):
        try:
            with open(self.config_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_settings(self):
        self.config_data['AI_URL'] = self.url_edit.text()
        self.config_data['AI_KEY'] = self.key_edit.text()
        try:
            with open(self.config_file, 'w', encoding='utf-8') as file:
                json.dump(self.config_data, file, indent=4)
            QMessageBox.information(self, "成功", "设置保存并更新成功.")
        except IOError as e:
            QMessageBox.critical(self, "错误", f"设置错误: {e}")