
#pyinstaller --noconfirm --onefile --windowed --icon "G:\wwwroot\aimsg2.1\logo.ico" --name "壳林智能客服助手" --add-data "G:\wwwroot\aimsg2.1\src\ChatPage.py;." --add-data "G:\wwwroot\aimsg2.1\src\HomePage.py;." --add-data "G:\wwwroot\aimsg2.1\src\LogPage.py;." --add-data "G:\wwwroot\aimsg2.1\src\MainWindow.py;." --add-data "G:\wwwroot\aimsg2.1\src\MessageProcessor.py;." --add-data "G:\wwwroot\aimsg2.1\src\SettingsPage.py;." --add-data "G:\wwwroot\aimsg2.1\utils\utils.py;." --add-data "G:\wwwroot\aimsg2.1\utils;utils/" --add-data "G:\wwwroot\aimsg2.1\src;src/" --add-data "G:\wwwroot\aimsg2.1\static;static/"  "G:\wwwroot\aimsg2.1\app.py"
import sys
import os
import logging

import src.MainWindow as MainWindow
from datetime import datetime
from PyQt6.QtWidgets import QApplication


    
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


# 启动应用
try:
    # 启动应用
    app = QApplication(sys.argv)
    window = MainWindow.MainWindow()
    sys.exit(app.exec())
except Exception as e:
    logger.error("应用启动失败", exc_info=True)
