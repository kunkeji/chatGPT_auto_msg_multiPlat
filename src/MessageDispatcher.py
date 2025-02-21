from PySide6.QtCore import QObject, Signal

class MessageDispatcher(QObject):
    message_received = Signal(str)  # 定义一个接收字符串消息的信号from PySide6.QtCore import QObject, pyqtSignal

