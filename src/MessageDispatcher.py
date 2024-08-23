from PyQt6.QtCore import QObject, pyqtSignal

class MessageDispatcher(QObject):
    message_received = pyqtSignal(str)  # 定义一个接收字符串消息的信号
