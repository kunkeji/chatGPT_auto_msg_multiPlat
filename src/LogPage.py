
from PyQt6.QtWidgets import  QWidget, QVBoxLayout, QTextEdit

from ttkbootstrap.constants import *

#日志
class LogPage(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        self.log_widget = QTextEdit()
        self.log_widget.setReadOnly(True)
        self.log_widget.setStyleSheet("background-color: white; border: 1px solid gray;")
        layout.addWidget(self.log_widget)
        self.setLayout(layout)

    def append_log_message(self, message):
        self.log_widget.append(message)