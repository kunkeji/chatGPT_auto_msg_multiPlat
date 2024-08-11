
from PyQt6.QtWidgets import QWidget,QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

from ttkbootstrap.constants import *

from config.Config import Config

config = Config()

class ChatPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("这是聊天页面", alignment=Qt.AlignmentFlag.AlignCenter))
        self.setLayout(layout)