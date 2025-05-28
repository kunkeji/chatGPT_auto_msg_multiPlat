from data.database_manager import DatabaseManager

from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt, QModelIndex, Slot, QCoreApplication, QTimer
from PySide6.QtWidgets import QMessageBox, QMainWindow, QGraphicsDropShadowEffect, QTableWidgetItem, QMenu, QTableWidgetItem, QListWidget, QVBoxLayout, QApplication, QPushButton
from PySide6.QtGui import QAction, QColor

from src.WebSocketServer import WebSocketServer
from src.MessageDispatcher import MessageDispatcher
from src.Message import Message
from flask import Flask, send_file, request, jsonify
from flask_sslify import SSLify
from threading import Lock, Thread
from pathlib import Path

from src.ui.home import Ui_MainWindow
from src.ui.login import Ui_LoginPage
from src.Updata import Updata

import webbrowser
import requests
import threading
import pyautogui
import json
import threading
import queue
import requests
import os
import ssl
import time
import signal
import requests
import webbrowser
import sys
import win32gui
import win32con
import win32api
import win32process

task_queue = queue.Queue()
flask_app = None
ws_server = None
current_version = "1.0.0.13"

# 登录
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 实例化 Ui_MainWindow 并设置 UI
        db_manager = DatabaseManager()
        self.db = db_manager
        system_info = db_manager.get_system_info()
        self.sinfo = system_info

        self.ui = Ui_LoginPage()
        self.ui.setupUi(self)
        if self.sinfo[7]:
            self.ui.username.setText(self.sinfo[7])
        if self.sinfo[5] and self.sinfo[8]:
            self.ui.checkBox.setChecked(True)
            self.ui.password.setText(self.sinfo[8])
        if self.sinfo[6]:
            self.ui.checkBox_2.setChecked(True)

        self.ui.checkBox_2.clicked.connect(self.change_checkBox)
        self.ui.checkBox.clicked.connect(self.change_checkBox)
        self.ui.pushButton_3.clicked.connect(self.gotoregister)
        self.ui.pushButton_4.clicked.connect(self.gotoresetpwd)
        # 绑定登录事件
        self.ui.loginBut.clicked.connect(self.login)
        # 设置无标题窗口
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # 设置背景透明
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(10)  # 阴影的模糊半径
        shadow.setColor(QColor(0, 0, 0, 255))  # 阴影的颜色和透明度
        shadow.setOffset(0, 0)  # 阴影的偏移量
        # 将阴影效果添加到按钮上
        self.ui.mainBox.setGraphicsEffect(shadow)
        self.ui.label_4.setText("版本号：" + current_version)
        self.delayed_login_timer = QTimer(self)
        self.delayed_login_timer.setSingleShot(True)  # 设置为单次触发
        self.delayed_login_timer.timeout.connect(
            self.check_and_login_if_needed)
        # 设置一个短暂的延迟，比如500毫秒
        self.delayed_login_timer.start(500)
        self.show()

    def check_and_login_if_needed(self):
        if self.sinfo[6]:  # 假设self.sinfo[6]为True时表示需要自动登录
            self.login()

    def change_checkBox(self):
        if self.ui.checkBox.isChecked():
            self.db.update_system_info(save_password=1)
        else:
            self.db.update_system_info(save_password=0)
        if self.ui.checkBox_2.isChecked():
            self.ui.checkBox.setChecked(True)
            self.db.update_system_info(auto_login=1)
            self.db.update_system_info(save_password=1)
        else:
            self.db.update_system_info(auto_login=0)

    def login(self):
        # 获取用户输入的用户名和密码
        username = self.ui.username.text()
        password = self.ui.password.text()
        # 数据验证
        if not username or not password:
            self.show_error_message("用户名和密码不能为空！")
            return
        # 构建请求数据
        data = {
            'account': username,
            'password': password
        }
        if self.ui.checkBox.isChecked() or self.ui.checkBox_2.isChecked():
            self.db.update_system_info(account=username)
            self.db.update_system_info(password=password)
        # 发起API请求
        response = requests.post('https://kelin.kunkeji.com/api/user/login', data=data)
        # 处理响应
        if response.status_code == 200:
            # 假设登录成功时，返回的JSON数据中有一个'success'字段为True
            response_data = response.json()
            if response_data['code'] == 1:
                userinfo = response_data['data']['userinfo']
                # 储存用户信息
                self.db.update_system_info(token=userinfo['token'])
                # 判断用户是否是会员
                if userinfo['vip'] == 1:
                    self.homewin = HomeWindow()
                    self.homewin.show()
                    self.close()
                else:
                    self.show_error_message(
                        "您还不是会员，请登录壳林官网(kelin.kunkeji.com)的会员中心购买！")
                # 这里可以添加登录成功后的操作，比如跳转到主界面
            else:
                self.show_error_message("登录失败，请检查用户名和密码！")
        else:
            self.show_error_message("登录请求失败，请稍后再试！")

    def show_error_message(self, message):
        # 显示错误消息
        msgbox = QMessageBox()
        msgbox.setIcon(QMessageBox.Information)
        msgbox.setText(message)
        msgbox.setStandardButtons(QMessageBox.Ok)
        msgbox.exec()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def gotoregister(self):
        # 打开指定网址
        webbrowser.open('https://kelin.kunkeji.com/index/user/register.html')

    def gotoresetpwd(self):
        # 打开指定网址
        webbrowser.open('https://kelin.kunkeji.com/index/user/login.html')


# 这里进行js注入工作，注入的js文件可以自行编写，也可以使用我们提供的kelin.js文件
# 监听服务
class FlaskApp:
    def __init__(self,userinfo):
        self.app = Flask(__name__)
        self.sslify = SSLify(self.app, permanent=True)
        self.userinfo = userinfo
        self.run_dir = os.path.dirname(os.path.abspath(__file__))
        self.lock = Lock()
        self.ui = Ui_MainWindow()
        @self.app.route("/imsupport")
        def inject_js():
            js_resource_path = os.path.join(
                self.run_dir, "./src/plugins/kelin.js")
            return send_file(js_resource_path, mimetype='application/javascript')

    def modify_hosts(self):
        hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
        try:
            # 尝试以管理员权限打开文件
            with open(hosts_path, 'r+', encoding='utf-8') as file:
                hosts_content = file.read()
                new_entry = "127.0.0.1 iseiya.taobao.com\n"
                if new_entry not in hosts_content:
                    file.seek(0, 2)
                    file.write(new_entry)
        except PermissionError:
            # 如果没有权限，显示提示信息
            print("请使用管理员权限运行程序。")
            # QMessageBox.warning(None, "权限错误", "请使用管理员权限运行程序。")
            return False
        except Exception as e:
            print(f"修改hosts文件时发生错误: {e}")
            return False
        return True

    def start_https_server(self, cert_path, key_path):
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile=cert_path, keyfile=key_path)
        try:
            http_thread = Thread(target=lambda: self.app.run(
                port=443, ssl_context=context))
            http_thread.start()
            print("启动成功")
            return True
        except Exception as e:
            print(f"启动失败,请联系管理员{e}")
            return False

    def init_message_listener(self):
        with self.lock:
            self.modify_hosts()
            cert_file = os.path.join(self.run_dir, "./src/plugins/server.crt")
            key_file = os.path.join(self.run_dir, "./src/plugins/server.key")
            print(key_file, 61)
            if not os.path.exists(cert_file) or not os.path.exists(key_file):
                # 输出错误信息
                print(f"启动失败,请联系管理员")
                return False
            https_success = self.start_https_server(cert_file, key_file)
            return https_success

    def shutdown(self):
        os.kill(os.getpid(), signal.SIGINT)

    def run(self):
        if not self.init_message_listener():
            print("消息监听初始化失败")
        else:
            while True:
                if self.userinfo['vip'] == 1:
                    time.sleep(1)

# 首页
class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 实例化 Ui_MainWindow 并设置 UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        db_manager = DatabaseManager()
        self.db = db_manager
        self.system_info = self.db.get_system_info()                    # 获取系统信息
        self.userinfo = self.db.get_userinfo(self.system_info[11])      # 获取用户信息              线上了

        self.keywords = self.db.get_keywords()                          # 获取关键词列表
        self.keywordskv = self.extract_keys(self.keywords)              # 提取关键词列表

        self.minganciData = self.db.get_sensitive()                     # 获取敏感词列表
        self.minganciDatakv = self.extract_keys(self.minganciData)      # 提取敏感词列表

        self.goodsList = self.db.get_goodslist()                        # 获取商品列表
        self.ui.username.setText(self.userinfo['nickname'])
        self.ui.emall.setText(self.userinfo['email'])
        self.ui.phone.setText(self.userinfo['mobile'])
        self.ui.birthday.setText(self.userinfo['birthday'])
        # 设置无标题窗口
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # 设置背景透明
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(10)  # 阴影的模糊半径
        shadow.setColor(QColor(0, 0, 0, 255))  # 阴影的颜色和透明度
        shadow.setOffset(0, 0)  # 阴影的偏移量
        # 将阴影效果添加到按钮上
        self.ui.home.setGraphicsEffect(shadow)
        # 绑定按钮的点击事件
        # lambda:self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_but.clicked.connect(lambda: self.munuBut(0))
        self.ui.massg_but.clicked.connect(lambda: self.munuBut(1))          # 敏感词按钮
        self.ui.keyword_but.clicked.connect(lambda: self.munuBut(2))        # 关键词按钮
        self.ui.setup_but.clicked.connect(lambda: self.munuBut(3))
        self.ui.my_but.clicked.connect(lambda: self.munuBut(4))

        self.ui.pushButton_2.clicked.connect(self.connectqianniu)
        self.ui.pushKeyword.clicked.connect(self.add_new_keyword)           # 关键词添加按钮
        # self.ui.pushKeyword_2.clicked.connect(self.add_new_keyword)       # 关键词添加按钮

        self.ui.mgctianjia.clicked.connect(self.add_new_sensitive)          # 敏感词添加按钮
        self.ui.updataBut.clicked.connect(self.updata_hosts)                # 系统设置保存按钮
        self.ui.cloerBut.clicked.connect(self.logout)                       # 系统设置退出按钮
        self.ui.newgoodsBut.clicked.connect(self.add_new_goods)             # 添加商品说明书
        self.ui.refresh.clicked.connect(self.get_goods_list)                # 刷新商品说明书

        self.ui.modify.clicked.connect(lambda: self.openweb('https://kelin.kunkeji.com/index/user/index.html'))
        self.ui.about.clicked.connect(lambda: self.openweb('https://kelin.kunkeji.com'))
        # 商品说明书--已完善
        self.goodsList = []
        self.listWidget = QListWidget()
        self.ui.listView.setModel(self.listWidget.model())
        layout = QVBoxLayout()
        layout.addWidget(self.ui.listView)
        # 商品说明书--未完善
        self.listWidget2 = QListWidget()
        self.ui.listView2.setModel(self.listWidget2.model())
        layout2 = QVBoxLayout()
        layout2.addWidget(self.ui.listView2)
        
        self.get_goods_list()
        self.setLayout(layout)
        self.setLayout(layout2)
        self.ui.listView.doubleClicked.connect(self.on_item_clicked)
        self.ui.listView2.doubleClicked.connect(self.on_item_clicked)
        
        # 加载关键词
        self.keyword_table = self.ui.tableWidget
        self.keyword_table.setColumnWidth(0, 100)
        self.keyword_table.setColumnWidth(1, 288)
        self.populate_table(self.keyword_table)
        self.keyword_table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.keyword_table.customContextMenuRequested.connect(lambda pos: self.showContextMenu(pos, self.keyword_table))
        self.keyword_table.itemChanged.connect(self.item_changed)
        self.minganciTable = self.ui.minganciTable
        self.minganciTable.setColumnWidth(0, 180)
        self.minganciTable.setColumnWidth(1, 200)
        self.populate_tablea()
        self.minganciTable.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.minganciTable.customContextMenuRequested.connect(self.showContextMenuM)
        self.minganciTable.itemChanged.connect(self.minganci_changed)

        # 初始化系统设置
        self.ui.tishici.setText(self.system_info[9])
        self.ui.tishici2.setText(self.system_info[10])
        self.show()
        self.append_log_message(f"{self.userinfo['nickname']}登录成功")

        # 获取config.json文件中的配置信息
        with open('config.json', 'r') as f:
            config = json.load(f)
        self.pipeidu = config["pipeidu"]
        # 设置匹配度
        self.ui.pipeidu.setValue(self.pipeidu)
        # 绑定滑动事件
        self.ui.pipeidu.sliderMoved.connect(self.on_slider_moved)

        self.flask_thread = None
        self.ws_thread = None
        self.dispatcher = MessageDispatcher()
        
        flask_thread = threading.Thread(target=self.run_flask)
        flask_thread.start()
        ws_thread = threading.Thread(target=self.run_websocket)
        ws_thread.start()
        # 增加线程循环任务
        loop_task  =threading.Thread(target=self.loop_task)
        loop_task.start()
        # 注入结束
        # 监听websocket服务
        self.dispatcher.message_received.connect(self.on_message_received)
        self.connectqianniu()# 连接千牛

        # 添加线程池和消息队列
        self.message_queue = queue.Queue()
        self.max_workers = 5  # 最大工作线程数
        self.worker_threads = []
        self.is_running = True
        
        # 启动工作线程
        for _ in range(self.max_workers):
            worker = threading.Thread(target=self.message_processor)
            worker.daemon = True
            worker.start()
            self.worker_threads.append(worker)

        # 添加拼多多客服按钮
        self.ui.pdd_button = QPushButton("拼", self)
        self.ui.pdd_button.setStyleSheet("""
            QPushButton {
                background-color: #E02020;
                color: white;
                border-radius: 4px;
                padding: 5px 15px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #FF2020;
            }
        """)
        self.ui.pdd_button.clicked.connect(self.open_pdd_window)
        self.ui.horizontalLayout.addWidget(self.ui.pdd_button)
        
        # 初始化浏览器窗口和测试服务器
        self.browser_window = None
        self.test_server_thread = None

    def open_pdd_window(self):
        """打开拼多多客服窗口"""
        from src.ui.browser import BrowserWindow
        from src.test_server import run_test_server
        import threading
        
        # 启动测试服务器（如果还没启动）
        if not self.test_server_thread:
            self.test_server_thread = threading.Thread(target=run_test_server, daemon=True)
            self.test_server_thread.start()
        
        # 创建新的浏览器窗口（如果还没创建）
        if not self.browser_window:
            self.browser_window = BrowserWindow()
        
        # 显示窗口
        self.browser_window.show()
        self.browser_window.raise_()

    # 循环任务
    def loop_task(self):
        while True:
            try:
                self.avoid_send_failure()
                # self.update_goods_list()
            except Exception as e:
                print(e)
    # 滑动事件
    def on_slider_moved(self, event):
        value = self.ui.pipeidu.value()
        # 将值传递给config.json文件
        with open('config.json', 'w') as f:
            json.dump({'pipeidu': value}, f)
        self.pipeidu = value

    def extract_keys(self, keyword_list):
        if keyword_list is None:
            return {}
        else:
            return {keyword['key']: keyword['value'] for keyword in keyword_list}

    # 打开指定网页
    def openweb(self, url):
        webbrowser.open(url)

    # 菜单样式重置
    def reset_menu_style(self):
        self.ui.home_but.setStyleSheet("image: url(:/icon/icon/首页.png);background-image:none;")
        self.ui.massg_but.setStyleSheet("image: url(:/icon/icon/敏感词.png);background-image: none;")
        self.ui.keyword_but.setStyleSheet("image: url(:/icon/icon/minganci.png);background-image: none;")
        self.ui.setup_but.setStyleSheet("image: url(:/icon/icon/设置.png);background-image: none;")
        self.ui.my_but.setStyleSheet("image: url(:/icon/icon/我的.png);background-image: none;")

    # 左侧菜单点击事件
    def munuBut(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)
        if index == 0:
            # self.ui.home_top_title.setText("壳林智能客服")
            self.reset_menu_style()
            self.ui.home_but.setStyleSheet("background-image: url(:/icon/icon/选中圆.png);image: url(:/icon/icon/首页.png);")
        elif index == 1:
            # self.ui.home_top_title.setText("敏感词管理")
            self.reset_menu_style()
            self.ui.massg_but.setStyleSheet("background-image: url(:/icon/icon/选中圆.png);image: url(:/icon/icon/敏感词.png);")
        elif index == 2:
            # self.ui.home_top_title.setText("商品说明书")
            self.reset_menu_style()
            self.ui.keyword_but.setStyleSheet("background-image: url(:/icon/icon/选中圆.png);image: url(:/icon/icon/minganci.png);")
        elif index == 3:
            # self.ui.home_top_title.setText("系统设置")
            self.reset_menu_style()
            self.ui.setup_but.setStyleSheet("background-image: url(:/icon/icon/选中圆.png);image: url(:/icon/icon/设置.png);")
        else:
            # self.ui.home_top_title.setText("个人中心")
            self.reset_menu_style()
            self.ui.my_but.setStyleSheet("background-image: url(:/icon/icon/选中圆.png);image: url(:/icon/icon/我的.png);")

    # 连接千牛
    def connectqianniu(self):
        # 首先获取父窗口句柄
        parent_hwnd = win32gui.FindWindow("Qt5152QWindowIcon", "千牛接待台")
        # 如果没有找到窗口，则寻找千牛客户端并打开
        if not parent_hwnd:
            os.startfile("aliim:login")
        else:
            # 显示窗口
            win32gui.ShowWindow(parent_hwnd, win32con.SW_SHOWMAXIMIZED)
            time.sleep(0.5)
            child_hwnd = self.find_child_window(parent_hwnd, "千牛工作台",2)
            print(child_hwnd,439)
            rect = win32gui.GetWindowRect(child_hwnd)
            x = rect[0]
            y = rect[1]
            # 计算相对于窗口的点击位置
            click_x = x + 10
            click_y = y + 10
            # 使用 pyautogui 移动鼠标并点击
            pyautogui.click(click_x, click_y)
            # 模拟点击F5
            pyautogui.hotkey('f5')
    
    
    # 避免发送失败事件
    def avoid_send_failure(self):
        while True:
            class_name = "Qt5152QWindowIcon"
            title_substring = "服务态度提醒"
            windows = self.find_window(class_name, title_substring)
            if windows:
                hwnd = windows[0]
                win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # 还原窗口
                win32gui.SetForegroundWindow(hwnd)  # 激活窗口
                time.sleep(0.5)  # 等待窗口激活

                # 计算相对位置并点击
                self.doClick(hwnd,290,200)
                # pyautogui.click(x, y)
                time.sleep(0.5)
                # 点击回车
                pyautogui.press('enter')

    def find_child_window(self,parent_handle, child_window_title, index=1):
        def callback(hwnd, hwnds):
            if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
                hwnds.append(hwnd)
            return True

        hwnds = []
        win32gui.EnumChildWindows(parent_handle, callback, hwnds)

        matched_hwnds = []
        for hwnd in hwnds:
            if win32gui.GetWindowText(hwnd) == child_window_title:
                matched_hwnds.append(hwnd)
            child_hwnd = self.find_child_window(hwnd, child_window_title, index)
            if child_hwnd:
                matched_hwnds.append(child_hwnd)

        if len(matched_hwnds) >= index:
            print(matched_hwnds,489)
            # 返回最后一个
            return matched_hwnds[len(matched_hwnds)-1]
        return None

    # 查找窗口
    def find_window(self,class_name, title):
        def enum_windows(hwnd, results):
            if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
                if win32gui.GetClassName(hwnd) == class_name and title in win32gui.GetWindowText(hwnd):
                    results.append(hwnd)

        hwnds = []
        win32gui.EnumWindows(lambda hwnd, _: enum_windows(hwnd, hwnds), None)
        return hwnds

    # 检测右下角窗口是否存在
    def check_bottom_window(self):
        pass

    # 获取商品的说明书列表
    def get_goods_list(self):
        self.listWidget.clear()
        self.listWidget2.clear()
        self.goodsList = self.db.get_goodslist()
        weinub = 0
        if self.goodsList:
            for item in self.goodsList:
                # 根据type字段判断是否是已完善的商品
                if item['type'] == 1:
                    self.listWidget.addItem(item['product_name'])
                else:
                    self.listWidget2.addItem(item['product_name'])
                    weinub = weinub + 1
            if weinub == 0:
                self.listWidget2.addItem("用户询问的商品完善完啦~")
        else:
            self.listWidget.addItem("暂无数据,请点击下方添加按钮添加")
        
    @Slot(QModelIndex)
    def on_item_clicked(self, index):
        # 获取被点击的项的文本
        item = self.listWidget.itemFromIndex(index)
        type = 1
        if item is None:
            type = 0
            item = self.listWidget2.itemFromIndex(index)
        # 判断是否有这个商品
        if not any(item.text() == good['product_name'] for good in self.goodsList):
            self.show_error_message("没有该商品")
            return
        # 判断商品item商品名在goodsList的下标
        goodsindex = next(i for i, good in enumerate(self.goodsList) if good['product_name'] == item.text())

        self.add_new_goods(self.goodsList[goodsindex]['id'],type=type)

    # 退出登录
    def logout(self, event):
        apiurl = 'https://kelin.kunkeji.com/api/user/logout'
        token = self.system_info[11]
        headers = {'token': f'{token}'}
        r = requests.post(apiurl, headers=headers)
        response_data = r.json()
        if response_data['code'] == 1:
            self.db.update_system_info(auto_login=0)
            self.append_log_message("退出成功")
            self.closeEvent(event)
            QMessageBox.information(self, "提示", '退出成功')
            self.close()
        else:
            self.show_error_message(f'退出失败')

    # 添加商品说明书
    def add_new_goods(self, goodsid=None,type=1):
        from src.newgoods import NewGoods
        
        self.newgoods = NewGoods(self.db, goodsid,type)
        self.newgoods.goodsAdded.connect(self.get_goods_list)
        self.newgoods.show()

    # 保存系统设置
    def updata_hosts(self):
        paiurl = self.ui.tishici.toPlainText()
        apikey = self.ui.tishici2.toPlainText()
        self.db.update_system_info(fastgpt_address=paiurl)
        self.db.update_system_info(fastgpt_key=apikey)
        QMessageBox.critical(self, "成功", '保存成功')

    # 弹出错误信息
    def show_error_message(self, message):
        # 显示错误消息
        QMessageBox.critical(self, "错误", message)

    # 开启flask服务
    def run_flask(self):
        global flask_app
        flask_app = FlaskApp(self.userinfo)
        flask_app.run()

    # 开启websocket服务
    def run_websocket(self):
        global ws_server
        ws_server = WebSocketServer(self.dispatcher, self.ui)
        ws_server.run()

    # 执行发送消息
    def sendMassage(self):
        # 查找千牛接待台窗口
        hWnd = win32gui.FindWindowEx(0, 0, "Qt5152QWindowIcon", "千牛接待台")
        if not hWnd:
            print("未找到千牛接待台窗口")
            return False
        # 获取当前焦点窗口
        current_focus = win32gui.GetForegroundWindow()
        # 如果窗口最小化，恢复窗口
        if win32gui.IsIconic(hWnd):
            win32gui.ShowWindow(hWnd, win32con.SW_RESTORE)
        # 尝试将焦点设置到千牛窗口
        try:
            # 获取当前线程和目标窗口线程
            current_thread = win32api.GetCurrentThreadId()
            target_thread = win32process.GetWindowThreadProcessId(hWnd)[0]
            # 附加线程输入状态
            win32process.AttachThreadInput(current_thread, target_thread, True)
            # 将窗口带到前台
            win32gui.SetForegroundWindow(hWnd)
            # 确保窗口可见
            win32gui.ShowWindow(hWnd, win32con.SW_SHOW)
            
            # 给窗口设置焦点
            win32gui.SetFocus(hWnd)
            
            # 解除线程输入状态附加
            win32process.AttachThreadInput(current_thread, target_thread, False)
            
            # 等待窗口获得焦点
            time.sleep(0.1)
            
            # 检查窗口是否真的获得了焦点
            if win32gui.GetForegroundWindow() == hWnd:
                # 使用 win32api 发送回车键
                print('发送回车键')
                win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)  # 按下
                time.sleep(0.05)
                win32api.keybd_event(win32con.VK_RETURN, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放
                return True
            else:
                print("无法获取窗口焦点")
                return False
                
        except Exception as e:
            print(f"发送消息时出错: {str(e)}")
            return False
        # finally:
        #     # 如果之前有其他窗口在前台，尝试恢复
        #     if current_focus and current_focus != hWnd:
        #         try:
        #             win32gui.SetForegroundWindow(current_focus)
        #         except:
        #             pass

    def message_processor(self):
        while self.is_running:
            try:
                # 从队列获取消息，设置超时以便能够响应关闭信号
                message = self.message_queue.get(timeout=1)
                if message is None:
                    continue
                    
                try:
                    processed_data = self.process_data(message)
                    if processed_data is not None:
                        self.send_to_client(processed_data)
                except Exception as e:
                    print(f"处理消息时出错: {str(e)}")
                finally:
                    self.message_queue.task_done()
                    
            except queue.Empty:
                continue
            except Exception as e:
                print(f"消息处理器出错: {str(e)}")
                continue

    def on_message_received(self, message):
        try:
            messages = json.loads(message)
            if json.loads(messages['message']) == 'send':
                self.sendMassage()
            else:
                # 将消息放入队列而不是直接创建新线程
                self.message_queue.put(messages)
                
        except KeyboardInterrupt:
            print("程序被用户中断，正在执行清理工作...")
            self.closeEvent(None)
        except Exception as e:
            print(f"接收消息时出错: {str(e)}")

    # 模拟点击
    def doClick(self,hwnd, cx, cy):
        Long_position = win32api.MAKELONG(cx, cy)
        win32api.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, Long_position)
        time.sleep(0.1)
        win32api.PostMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, Long_position)
   
    # 处理消息
    def process_data(self, message_data):
        # 获取客户端ID
        M = Message(self.db)
        client_id = message_data['client_id']
        # 将消息内容从JSON字符串解析为字典
        message_data = json.loads(message_data['message'])
        if message_data['direction']:
            M.save_chatlog(message_data)
        else:
            # 接收并处理消息
            cent = self.loadInformation(message_data)
            M.save_chatlog(message_data)
            # 敏感词替换
            if cent is not None:
                for word, replacement in self.minganciDatakv.items():
                    cent = cent.replace(word, replacement)
                client_object = message_data['fromid']['nick']
                # 获取发送方账号昵称
                account = message_data['toid']['nick']
                if client_object == '' or account == '':
                    return None
                if message_data['loginid']['nick'] == message_data['fromid']['nick']:
                    return None
                url_protocol = f'aliim:sendmsg?touid=cntaobao{client_object}&uid=cntaobao{account}'
                # 打开连接
                webbrowser.open(url_protocol)
                print(url_protocol,'打开连接')
                data = {
                    'client_id': client_id,
                    'user': client_object,
                    'msg': cent,
                    'url': url_protocol
                }
                return data
            else:
                return None

    # 本地信息处理
    def loadInformation(self, message_data):
        M = Message(self.db,self.ui)
        ccode = message_data.get('ccode')
        # 获取会话信息
        chatinfo = self.db.get_association(message_data)
        # 判断会话是否绑定商品
        # 判断chatinfo['goodsinfo']是否纯在，如果存在，则赋值给goodsinfo变量
        if chatinfo and 'goodsinfo' in chatinfo:
            goodsinfo = chatinfo['goodsinfo']
        else:
            goodsinfo = None

        try:
            msg_type = message_data['originalData'].get('msgtype')
            template_id = message_data['templateId']
            # 辅助函数用于构建数据字典
            def build_data(goodsinfo=goodsinfo, **kwargs):
                base_data = {
                    "goodsinfo": goodsinfo,
                    "userid": message_data['fromid']['targetId'],
                    "username": message_data['fromid']['nick'],
                    "havMainId": message_data['loginid']['havMainId'],
                    "kefuid": message_data['toid']['targetId'],
                    "kefuname": message_data['toid']['nick'],
                    "goodsname": message_data['originalData']['goodsname'],
                    "url":message_data['originalData']['url'],
                    "ccode": ccode,
                }
                base_data.update(kwargs)
                return base_data
            if template_id == 101:  # 文字消息
                if msg_type == 'sysmsg':
                    return M.sysmessage()
                elif msg_type == 'text':
                    data = build_data(message=message_data['originalData']['message'])
                    return M.textmessage(data)
                elif msg_type == 'link':
                    urlinfo = json.loads(message_data['originalData']['urlinfo'])
                    data = build_data(goodsname=urlinfo['title'])
                    return M.linkmessage(data)
                elif msg_type == 'face':
                    return M.facemessage(message_data['originalData']['message'])
                elif msg_type == 'urllink':
                    data = build_data(message=message_data['originalData']['message'])
                    return M.urllinkmessage(data)
            elif template_id == 332001:                                                                 # 通过链接进入消息界面
                data = build_data(goodsname=message_data['originalData']['goodsname'],url=message_data['originalData']['url'])
                return M.linkmessage(data)
            elif template_id == 129:                                                                    # 发送带有规格信息的产品链接
                data = build_data(itemSku=message_data['originalData']['itemSku'], goodsname=message_data['originalData']['goodsname'])
                return M.linkmessage(data)

        except KeyError as e:
            print(f"Missing key in message_data - {e}")
            return None

        except Exception as e:
            print(f"出错了: {e}")
            return None

    # 将处理过的数据加入到队列
    def add_to_queue(self, processed_data, client_queue):
        client_queue.put(processed_data)

    # 线程工作函数，用于处理数据并加入队列
    def thread_worker(self, data):
        processed_data = self.process_data(data)
        if processed_data is not None:
            self.send_to_client(processed_data)
    # 向客户端发送数据
    def send_to_client(self, data):
        # 这里实现发送数据的逻辑
        ws_server.send_message(data['client_id'], json.dumps(data))
        self.sendMassage();

    # 关键词：添加关键词列表数据
    def populate_table(self, table):
        if self.keywords is not None:
            table.setRowCount(len(self.keywords))
            row = 0
            if len(self.keywords) > 0:
                for item in self.keywords:
                    table.setItem(row, 0, QTableWidgetItem(item['key']))
                    table.setItem(row, 1, QTableWidgetItem(item['value']))
                    row += 1

    # 关键词：显示右键菜单
    def showContextMenu(self, pos, table):
        contextMenu = QMenu(self)
        deleteAction = QAction("删除选中", self)
        deleteAction.triggered.connect(lambda: self.deleteItem(table))
        contextMenu.addAction(deleteAction)
        contextMenu.exec(table.mapToGlobal(pos))

    # 关键词：删除选中项
    def deleteItem(self, table):
        index = table.currentRow()
        data = self.keywords[index]
        if index >= 0:
            self.db.delete_keyword(data['id'])
            del self.keywordskv[data['key']]
            table.removeRow(index)

    # 关键词：修改选中项
    def item_changed(self, item):
        row = item.row()
        data = self.keywords[row]
        key_item = self.keyword_table.item(row, 0)
        value_item = self.keyword_table.item(row, 1)
        if key_item.text() != data['key'] or value_item.text() != data['value']:
            self.db.update_keyword(
                data['id'], key_item.text(), value_item.text())
            self.keywordskv[key_item.text()] = value_item.text()
            del self.keywordskv[data['key']]
            self.keywords[row] = self.db.getkeyword(data['id'])

    # 关键词：添加新关键词
    def add_new_keyword(self):
        new_key = self.ui.new_key_edit.text().strip()
        new_value = self.ui.new_value_edit.text().strip()
        if new_key and new_value:
            if new_key in self.keywordskv or new_key in self.minganciDatakv:
                QMessageBox.warning(self, "重复关键词", f"这个关键词'{new_key}'已经添加过了.")

            else:
                # 添加并更新关键词列表
                if self.keyword_table.rowCount() == 0:
                    self.keywords = []
                    self.keywords.append(self.db.add_keyword(
                        new_key, new_value, type=1))
                else:
                    self.keywords.append(self.db.add_keyword(
                        new_key, new_value, type=1))
                self.keywordskv[new_key] = new_value
                row_position = self.keyword_table.rowCount()
                self.keyword_table.insertRow(row_position)
                self.keyword_table.setItem(
                    row_position, 0, QTableWidgetItem(new_key))
                self.keyword_table.setItem(
                    row_position, 1, QTableWidgetItem(new_value))
                self.ui.new_key_edit.clear()
                self.ui.new_value_edit.clear()
        else:
            QMessageBox.warning(self, "缺少输入", "请输入关键词和出发内容.")

    # 敏感词：显示右键菜单
    def showContextMenuM(self, pos):
        contextMenu = QMenu(self)
        deleteAction = QAction("删除选中", self)
        deleteAction.triggered.connect(self.deleteItemc)
        contextMenu.addAction(deleteAction)
        contextMenu.exec(self.minganciTable.mapToGlobal(pos))

    # 敏感词：修改选中项
    def minganci_changed(self, item):
        row = item.row()
        data = self.minganciData[row]
        key_item = self.minganciTable.item(row, 0)
        value_item = self.minganciTable.item(row, 1)
        if key_item.text() != data['key'] or value_item.text() != data['value']:
            self.db.update_keyword(
                data['id'], key_item.text(), value_item.text())
            self.minganciDatakv[key_item.text()] = value_item.text()
            del self.minganciDatakv[data['key']]
            self.minganciData[row] = self.db.getkeyword(data['id'])

    # 敏感词：删除选中项
    def deleteItemc(self):
        index = self.minganciTable.currentRow()
        data = self.minganciData[index]
        if index >= 0:
            self.db.delete_keyword(data['id'])
            del self.minganciDatakv[data['key']]
            self.minganciTable.removeRow(index)

    # 敏感词：添加敏感词
    def add_new_sensitive(self):
        new_key = self.ui.minganci.text().strip()
        new_value = self.ui.tihuan.text().strip()

        if new_key and new_value:
            if new_key in self.keywordskv or new_key in self.minganciDatakv:
                QMessageBox.warning(self, "重复关键词", f"这个关键词'{new_key}'已经添加过了.")
            else:
                if self.minganciTable.rowCount() == 0:
                    self.minganciData = []

                self.minganciData.append(
                    self.db.add_keyword(new_key, new_value, type=2))

                self.minganciDatakv[new_key] = new_value
                row_position = self.minganciTable.rowCount()
                self.minganciTable.insertRow(row_position)
                self.minganciTable.setItem(
                    row_position, 0, QTableWidgetItem(new_key))
                self.minganciTable.setItem(
                    row_position, 1, QTableWidgetItem(new_value))

                self.ui.minganci.clear()
                self.ui.tihuan.clear()
        else:
            QMessageBox.warning(self, "缺少输入", "请输入关键词和出发内容.")

    # 敏感词：输出表格
    def populate_tablea(self):
        if self.minganciData is not None:
            self.minganciTable.setRowCount(len(self.minganciData))
            row = 0
            for key, value in self.minganciDatakv.items():
                self.minganciTable.setItem(row, 0, QTableWidgetItem(key))
                self.minganciTable.setItem(row, 1, QTableWidgetItem(value))
                row += 1

    # 输出添加首页日志
    def append_log_message(self, message):
        self.ui.textEdit.append(f"{message}")

    # 页面拖动方法
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    # 页面拖动方法
    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
            mouse_event.accept()

    # 页面拖动方法
    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    # 关闭程序时关闭所有服务器
    def closeEvent(self, event):
        # 设置关闭标志
        self.is_running = False
        # 等待所有消息处理完成
        self.message_queue.join()
        # 清理工作线程
        for _ in self.worker_threads:
            self.message_queue.put(None)  # 发送终止信号
        for worker in self.worker_threads:
            worker.join(timeout=1)
            
        # 关闭其他服务
        if ws_server:
            print("正在关闭 WebSocket 服务器...")
            ws_server.stop_server()
        if flask_app:
            flask_app.shutdown()

        print("所有服务器已关闭，程序退出。")
        if event:
            event.accept()
            super().closeEvent(event)

# 检测版本更新
def check_for_updates():
    # 定义线上版本信息接口的URL
    version_check_url = 'https://kelin.kunkeji.com/api/version/index'
    # 发送POST请求以获取线上版本信息
    response = requests.post(version_check_url)
    # 检查响应状态码
    if response.status_code == 200:
        version_data = response.json()
        # 检查线上是否有新版本
        for row in version_data['data']['rows']:
            if row['oldversion'] == current_version and row['status'] == 'normal':
                # 线上版本较新，提示用户升级
                return False
            else:
                return True
    else:
        print("无法获取线上版本信息，请稍后再试。")
if __name__ == '__main__':
    db_manager = DatabaseManager()
    system_info = db_manager.get_system_info()      # 本地系统缓存信息
    app = QApplication(sys.argv)
    # 首先弹出启动画面
    # 在显示    窗口之前，检查版本更新
    if check_for_updates():
        login = LoginWindow()
        login.show()
    else:
        updata = Updata(current_version)
        updata.show()
    sys.exit(app.exec())
