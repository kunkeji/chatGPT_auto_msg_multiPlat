from src.ui.updata import Ui_UpData
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QColor, QCursor, QPainter, QBrush, QPen, QFont, QMouseEvent
from PySide6.QtWidgets import QGraphicsDropShadowEffect
from PySide6.QtCore import QThread, Signal
import os
import requests
from tqdm import tqdm
import subprocess


class DownloadThread(QThread):
    progress_signal = Signal(int)  # 用于更新进度条的信号
    finished_signal = Signal(str)  # 下载完成信号，传递文件路径

    def __init__(self, url, output_path):
        super().__init__()
        self.url = url
        self.output_path = output_path

    def run(self):
        # 下载安装包并将下载进度通过信号发出
        response = requests.get(self.url, stream=True)
        if response.status_code != 200:
            print(f"Error: Unable to download file from {self.url}")
            return

        total_size = int(response.headers.get('content-length', 0))
        with open(self.output_path, 'wb') as file:
            for data in response.iter_content(chunk_size=1024):
                if data:
                    file.write(data)
                    progress = (file.tell() / total_size) * 100
                    self.progress_signal.emit(progress)  # 发出进度更新信号

        self.finished_signal.emit(self.output_path)  # 下载完成，发出完成信号



class Updata(QMainWindow):
    def __init__(self,version):
        super().__init__()
        # 实例化 Ui_MainWindow 并设置 UI
        self.ui = Ui_UpData()
        self.ui.setupUi(self)
        self.current_version = version
        # 设置无标题窗口
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 设置背景透明
        self.setAttribute(Qt.WA_TranslucentBackground)
        # 初始化拖动窗口的标志和位置
        self.m_flag = False
        self.m_Position = QPoint()
        # 添加阴影效果
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(10)  # 阴影的模糊半径
        shadow.setColor(QColor(0, 0, 0, 255))  # 阴影的颜色和透明度
        shadow.setOffset(0, 0)  # 阴影的偏移量
        self.ui.frame.setGraphicsEffect(shadow)
        # 获取新版本列表
        self.check_for_updates()
        # 获取最新安装包
        self.show()

    # 下载安装包并将下载进度赋值给进度条（self.ui.jindutiao.setValue）
    def download_file(self, url, output_path="./installer.exe"):
        # 创建下载线程实例
        self.download_thread = DownloadThread(url, output_path)
        
        # 连接信号到槽
        self.download_thread.progress_signal.connect(self.update_progress)
        self.download_thread.finished_signal.connect(self.on_download_finished)
        
        # 开始线程
        self.download_thread.start()

    def update_progress(self, progress):
        # 更新进度条的槽函数
        self.ui.jindutiao.setValue(progress)

    def on_download_finished(self, file_path):
        # 下载完成的槽函数
        self.open_file(file_path)
        self.close()
        
    def open_file(self,file_path):
        # 根据文件类型选择打开方式，这里以PDF为例，你可以根据需要修改这部分代码
        if file_path.endswith('.exe'):
            try:
                # 在Windows上打开PDF文件，你可以根据需要修改这部分代码以适应其他操作系统或文件类型
                os.startfile(file_path)
            except AttributeError:
                # 对于非Windows系统，可以使用subprocess模块打开文件
                subprocess.run(['open', '--', file_path], check=True)  # macOS示例，Linux可能需要修改为其他命令，如xdg-open等。
        else:
            print(f"Unsupported file type: {file_path}")


    # 检测版本更新
    def check_for_updates(self):
        # 定义线上版本信息接口的URL
        version_check_url = 'https://kelin.kunkeji.com/api/version/index'
        # 发送POST请求以获取线上版本信息
        response = requests.post(version_check_url)
        # 检查响应状态码
        if response.status_code == 200:
            version_data = response.json()
            # 检查线上是否有新版本
            for row in version_data['data']['rows']:
                if row['oldversion'] == self.current_version and row['status'] == 'normal':
                    # 线上版本较新，提示用户升级
                    self.download_file(row['downloadurl'],f'{row["newversion"]}.exe')
        else:
            print("无法获取线上版本信息，请稍后再试。")

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton and not self.isMaximized():
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, event: QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(event.globalPos() - self.m_Position)  # 更改窗口位置
            event.accept()

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    
