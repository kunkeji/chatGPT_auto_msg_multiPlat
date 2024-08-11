#src/MainWindow.py

import os
import logging
import win32gui
import time
import json
import pyautogui
import pyperclip
import re
import src.HomePage as HomePage
import src.LogPage as LogPage
import src.SettingsPage as SettingsPage
import src.ChatPage as ChatPage
import src.MessageProcessor as MP
from PyQt6.QtWidgets import QMainWindow,QWidget,QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QStackedWidget
from PyQt6.QtGui import QIcon, QPixmap, QCursor
from PyQt6.QtCore import Qt, QSize, QTimer
from ttkbootstrap.constants import *
from config.Config import Config
from utils.utils import doClick

config = Config()
STRINGS_TO_REMOVE =[
        "诈骗案件频发，谨防假客服欺诈！任何以不能下单或店铺有问题诱导卖家点击链接、文档或扫码跳转到微信、QQ、支付宝或其它非官方平台的行为都是欺诈。",
        "谨防“订单卡单退款”类电信诈骗，请勿透露银行卡密码、验证码等信息！",
        "阿里巴巴不会向用户索要任何密码信息，请注意保护您的隐私信息！",
        "请勿使用阿里旺旺、千牛以外的其它聊天工具，以确保沟通、交易的安全。",
        "消息可能包含存在未知风险的链接，请谨慎访问",
        "您好像还没有配置消费者问到的常见问题回答，为了提升您的接待效率、减少顾客流失，建议您尽快完善此配置 立即配置",
        "您接待过此消费者，为避免插嘴、抢答，机器人已暂停接待，>>点此【立即恢复接待】<<",
        "机器人未找到对应的回复，点击添加",
        "8-23点间，店铺需有客服在线，机器人才会接待消费者",
        "没有更多了",
        "使用“邀请下单”，可提前备注订单，轻松提升转化率！立即使用",
        "您好像还没有配置消费者问到的常见问题回答，为了提升您的接待效率、减少顾客流失，建议您尽快完善此配置 立即配置",
        "新消息"
    ]

# 配置日志记录器
logger = logging.getLogger('日志记录器')
logger.setLevel(logging.INFO)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.m_p = MP.MessageProcessor(self)

    def initUI(self):
        self.setWindowTitle(config.APP_NAME)
        self.setGeometry(100, 100, config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
        self.setFixedSize(config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        toolbar = QWidget()
        toolbar.setFixedWidth(60)
        toolbar.setStyleSheet("background-color: #343A40;")
        toolbar_layout = QVBoxLayout(toolbar)
        toolbar_layout.setContentsMargins(0, 15, 0, 15)
        toolbar_layout.setSpacing(0)
        logo_label = QLabel()
        pixmap = QPixmap(config.APP_ICON_PATH).scaled(45, 45, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        logo_label.setPixmap(pixmap)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        toolbar_layout.addWidget(logo_label)
        toolbar_layout.addSpacing(50)
        self.nav_buttons = []
        nav_labels = ['首页', '聊天', '日志', '设置']
        for i, icon_path in enumerate(config.ICON_PATHS):
            btn = QPushButton()
            btn.setIcon(QIcon(icon_path))
            btn.setIconSize(QSize(25, 25))
            btn.setFixedSize(25, 25)
            btn.setStyleSheet("background-color: transparent;")
            btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            btn.clicked.connect(lambda checked, label=nav_labels[i]: self.handle_button_click(label))
            self.nav_buttons.append(btn)
            toolbar_layout.addWidget(btn, alignment=Qt.AlignmentFlag.AlignCenter)
            toolbar_layout.addSpacing(30)
        toolbar_layout.addStretch()
        self.run_button = QPushButton()
        self.run_button.setIcon(QIcon("./static/image/icons/run.png"))
        self.run_button.setIconSize(QSize(25, 25))
        self.run_button.setFixedSize(25, 25)
        self.run_button.setStyleSheet("background-color: transparent;")
        self.run_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.run_button.clicked.connect(lambda: self.handle_button_click("运行"))
        toolbar_layout.addWidget(self.run_button, alignment=Qt.AlignmentFlag.AlignCenter)
        display = QStackedWidget()
        display.setStyleSheet("background-color: #FFCE67;")
        self.pages = {
            '首页': HomePage.HomePage(self),
            '聊天': ChatPage.ChatPage(),
            '日志': LogPage.LogPage(self),
            '设置': SettingsPage.SettingsPage()
        }
        for label, page in self.pages.items():
            display.addWidget(page)
        main_layout.addWidget(toolbar)
        main_layout.addWidget(display)
        for btn, label in zip(self.nav_buttons, nav_labels):
            btn.clicked.connect(lambda checked, lbl=label: display.setCurrentWidget(self.pages[lbl]))
        # 定时器
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.detect_messages)
        self.timer.start(500)
        
        self.pages['首页'].refresh_platform_status()
        self.show()

    def handle_button_click(self, label):
        if label == "运行":
            if not config.APP_RUN_STATE:
                config.APP_RUN_STATE = True
                self.log_message("运行按钮点击")
                self.change_run_button_icon("pause")
                self.timer.start(1000)  # 每秒检查一次
            else:
                config.APP_RUN_STATE = False
                self.log_message("暂停按钮点击")
                self.change_run_button_icon("run")
                self.timer.stop()

    def change_run_button_icon(self, state):
        if state == "pause":
            self.run_button.setIcon(QIcon("./static/image/icons/pause.png"))

        else:
            self.run_button.setIcon(QIcon("./static/image/icons/run.png"))

    def detect_messages(self):
        if config.APP_RUN_STATE:
            pyperclip.copy('')
            self.check_platform_messages()

    def check_platform_messages(self):
        if config.PDD_SELECT:
            self.check_pdd()
        if config.QN_SELECT:
            self.check_qn()
        if config.DD_SELECT:
            self.check_dd()
            
    def check_pdd(self):
        hwnd_to_click = win32gui.FindWindow(config.PDD_MSG_CLASS_NAME, config.PDD_MSG_TITLE)
        if win32gui.IsWindow(hwnd_to_click) and win32gui.IsWindowVisible(hwnd_to_click):
            self.log_message("检测到拼多多消息窗口")
            self.m_p.process_message('pdd', hwnd_to_click, (96, 63))

    def check_qn(self):
        hwnd_to_click = win32gui.FindWindow(config.QN_MSG_CLASS_NAME, config.QN_MSG_TITLE)
        if win32gui.IsWindow(hwnd_to_click) and win32gui.IsWindowVisible(hwnd_to_click):
            self.log_message("检测到千牛消息窗口")
            self.m_p.process_message('qn', hwnd_to_click, (130, 80))

    def check_dd(self):
        hwnd_to_click = win32gui.FindWindow(config.DD_MSG_CLASS_NAME, config.DD_MSG_TITLE)
        if win32gui.IsWindow(hwnd_to_click) and win32gui.IsWindowVisible(hwnd_to_click):
            self.log_message("检测到抖店消息窗口")
            self.m_p.process_message('dd', hwnd_to_click, (130, 80))



    def log_message(self, message):
        logger.info(message)
        self.pages['首页'].append_log_message(message)
        self.pages['日志'].append_log_message(message)
    
    def ppd_username(self):
        pyperclip.copy('')
        doClick(config.PDD_APP_HWND,420,145)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.2)
        username = pyperclip.paste()
        if username:
            pass
        else:
            username = self.generate_id()
            pyautogui.typewrite(username)
        return username
    
    def generate_id(self):
        timestamp = str(int(time.time()))
        return timestamp

    def pdd_patterntext(self,text):
        regex = r'\r\n商品ID：(\w+) 复制\r\n\r\n\r\n(.*?)(?=\r)(?:.*?)(?=头像|$)'
        # 定义一个替换函数
        def replacement(match):
            product_id, description = match.groups()
            return f"用户想询问商品：{description.strip()}商品id为：{product_id.strip()}"
        # 使用re.sub替换匹配的内容
        text = re.sub(regex, replacement, text, flags=re.DOTALL)

        regex = r'\r\n咨询商品规格\r\n\r\n(.*?)(?=\r\n)\r\n(.*?)(?=￥)￥\w+(?:\r\n头像|$)'
        def replacement(match):
            description,properties = match.groups()
            return f"用户想询问商品：{description.strip()}中{properties}规格的问题\r\n头像"
        text = re.sub(regex, replacement, text, flags=re.DOTALL)

        regex = r'\r\n当前用户来自 商品详情页\r\n\r\n(.*?)(?=￥)￥\w+(?:.*?)(?=头像|$)'
        def replacement(match):
            description = match.groups(0)
            return f"(用户来自商品“{description[0].strip()}”的商品详情页)"
        text = re.sub(regex, replacement, text, flags=re.DOTALL)

        pattern = r'已读|未读'
        matches = list(re.finditer(pattern, text))
        if matches:
            last_match = matches[-1]
            last_index = last_match.end()
            result = text[last_index:]
        else:
            result = text
        for phrase in STRINGS_TO_REMOVE:
            result = text.replace(phrase, "")
        return result

    def pdd_getquestionlist(self,text):
        text = self.pdd_patterntext(text)
        regex =  r"(?:头像)([^\r\n].*?|\r\n|$)(?=(?:$|\r\n头像)|(?:\d{1,2}:\d{1,2}:{1,2}))|(?:头像)\r\n([^\r\n].*?)(?=\r\n)\r\n(.*?)(?=(?:\d{1,2}:\d{1,2}:{1,2})|$|\r\n头像)"
        matches = re.findall(regex, text, re.DOTALL)
        filtered_messages = [
            {
                "botname": botname,
                "msg": botmsg.strip(),
                "role": "bot"
            } if botname else {
                "usermsg": uaermsg.strip() if uaermsg and uaermsg.strip() != "" and uaermsg.strip() != '\r\n' else '[图片信息]',
                "role": "user"
            }
            for uaermsg, botname, botmsg in matches
        ]
        json_data = json.dumps(filtered_messages, ensure_ascii=False, indent=4)
        data = json.loads(json_data)
        last_user_index = next((index for index, item in enumerate(reversed(data)) if item['role'] == 'bot'), None)
        if last_user_index is not None:
        # 因为data是反向遍历的，所以需要计算正向的索引
            last_user_index = len(data) - last_user_index - 1
            result = data[last_user_index+1:]
        else:
            result = []
        return result

    def qn_patterntext(self,text):

        pattern = r'已读|未读'
        matches = list(re.finditer(pattern, text))
        if matches:
            last_match = matches[-1]
            last_index = last_match.end()
            text = text[last_index:]
        else:
            text = text

        regex = r'\r\n\r\n(.*?)(?:\r\n月销.*?)(?:\r\n\r\n|$)'
        def replacement(match):
            description = match.groups(0)
            return f"\r\n我想咨询一下这个商品“{description[0].strip()}”\r\n"
        text = re.sub(regex, replacement, text, flags=re.DOTALL)

        regex = r'当前用户来自\r\n商品详情页\r\n\r\n(.*?)(?:\r\n¥\r\n\w+.\w+\r\n)'
        # 定义一个替换函数
        def replacement(match):
            description = match.groups(0)
            return f"\r\n我想咨询一下这个商品：{description}\r\n"
        # 使用re.sub替换匹配的内容
        text = re.sub(regex, replacement, text, flags=re.DOTALL)

        regex = r'\r\n我要咨询这个规格的商品\r\n\r\n(.*?)(?:\r\n)(.*?)(?:\r\n¥\r\n\w+\r\n.\w+\r\n)'
        def replacement(match):
            description,guige = match.groups()
            return f"\r\n我想咨询一下这个商品：{description}的{guige}这个规格\r\n"
        # 使用re.sub替换匹配的内容
        text = re.sub(regex, replacement, text, flags=re.DOTALL)
        for phrase in STRINGS_TO_REMOVE:
            text = text.replace(phrase, "")

        return text
    
    def qn_getquestionlist(self,text):
        text = self.qn_patterntext(text)
        pattern = r'(?m)(?:^(\d{4}-\d{1,2}-\d{1,2})\s+?(\d{1,2}:\d{1,2}:\d{1,2})(.*?)\n([\s\S]+?)(?=已读|未读|^.*?\d{4}-\d{1,2}-\d{1,2})|^(.*?)(\d{4}-\d{1,2}-\d{1,2})\s+?(\d{1,2}:\d{1,2}:\d{1,2})([\s\S]+?)\n(?:(?=^.*?\d{4}-\d{1,2}-\d{1,2})|(?=\d{4}-\d{1,2}-\d{1,2})|(?=$)))'
        # 匹配所有结果
        result = re.findall(pattern, text)
        filtered_messages = [
            {
                "name": name,
                "date": date,
                "time": time,
                "massage": message.strip() if message and message.strip() != "" and message.strip() != '\r\n' else '[图片信息]',
                "role": "staff"
            } if name else {
                "name": username,
                "date": userdata,
                "time": usertime,
                "massage": usermassage.strip() if usermassage and usermassage.strip() != "" and usermassage.strip() != '\r\n' else '[图片信息]',
                "role": "customer"
            }
            for date, time, name, message, username, userdata, usertime, usermassage in result
        ]
        json_data = json.dumps(filtered_messages, ensure_ascii=False, indent=4)
        return json.loads(json_data)



    