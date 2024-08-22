#pyinstaller --noconfirm --onefile --windowed --icon "G:\wwwroot\aimsg2.1\logo.ico" --name "壳林智能客服助手" --add-data "G:\wwwroot\aimsg2.1\src\ChatPage.py;." --add-data "G:\wwwroot\aimsg2.1\src\HomePage.py;." --add-data "G:\wwwroot\aimsg2.1\src\LogPage.py;." --add-data "G:\wwwroot\aimsg2.1\src\MainWindow.py;." --add-data "G:\wwwroot\aimsg2.1\src\MessageProcessor.py;." --add-data "G:\wwwroot\aimsg2.1\src\SettingsPage.py;." --add-data "G:\wwwroot\aimsg2.1\utils\utils.py;." --add-data "G:\wwwroot\aimsg2.1\utils;utils/" --add-data "G:\wwwroot\aimsg2.1\src;src/" --add-data "G:\wwwroot\aimsg2.1\static;static/"  "G:\wwwroot\aimsg2.1\app.py"
#auto-py-to-exe
import sys
import os
import logging
import threading
import src.FlaskApp as FlaskApp
import src.MainWindow as MainWindow
from datetime import datetime
from PyQt6.QtWidgets import QApplication
from src.WebSocketServer import WebSocketServer

# 创建日志目录
LOG_DIR = 'log'
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# 获取当前日期
current_date = datetime.now().strftime("%Y-%m-%d")
log_filename = os.path.join(LOG_DIR, f'{current_date}.log')

# 配置日志记录器
logger = logging.getLogger('日志记录器')
logger.setLevel(logging.INFO)

# 检查当前日期的日志文件是否存在，如果不存在则创建新的
if not os.path.exists(log_filename):
    with open(log_filename, 'w', encoding='utf-8'):
        pass

handler = logging.FileHandler(log_filename, encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

flask_app = None
ws_server = None

def run_flask():
    global flask_app
    flask_app = FlaskApp.FlaskApp()
    flask_app.run()

def run_websocket():
    global ws_server
    ws_server = WebSocketServer()
    ws_server.run()
# 启动应用
try:
    # 开启子程序Flask服务
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    
    # 开启WebSocket服务
    ws_thread = threading.Thread(target=run_websocket)
    ws_thread.start()
    # 启动应用
    app = QApplication(sys.argv)
    window = MainWindow.MainWindow(ws_server)

    # 监听主线程的退出信号
    def on_exit():
        logger.info("应用正在关闭...")
        if flask_app:
            flask_app.shutdown()  # 关闭Flask服务器
        if ws_server:
            ws_server.stop_server()  # 关闭WebSocket服务器
        flask_thread.join()  # 等待Flask线程安全关闭
        ws_thread.join()  # 等待WebSocket线程安全关闭

    app.aboutToQuit.connect(on_exit)
    sys.exit(app.exec())

except Exception as e:
    logger.error("应用启动失败", exc_info=True)
