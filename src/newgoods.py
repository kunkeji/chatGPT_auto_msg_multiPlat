from src.ui.newgoods import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow,QMessageBox
from PySide6 import QtCore, QtGui
import re

from PySide6.QtCore import Signal

class NewGoods(QMainWindow):
    goodsAdded = Signal()
    # 设置信号槽
    def __init__(self,db_manager,goodsid=None,type=1):
        super().__init__()
        # 实例化 Ui_MainWindow 并设置 UI
        # 获取商品信息
        self.db = db_manager
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.add.clicked.connect(self.add_goods)
        self.goods = None
        self.goodstype = type
        self.ui.delgoods.hide()
        if goodsid:
            self.goods = self.db.get_goodsByid(goodsid,type)
            self.init_info(self.goods)
            self.ui.Title.setText("修改商品")
            self.ui.add.setText("确认修改")
            self.ui.delgoods.clicked.connect(self.del_goods)
            self.ui.delgoods.show()

        #设置无标题窗口
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #设置背景透明
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # 绑定登录事件
        self.show()

    # 添加商品
    def add_goods(self):
        goodsurl = self.ui.goodsurl.text()
        goodsname = self.ui.goodsname.text()
        shopname = self.ui.shopname.text()
        welcome = self.ui.welcome.toPlainText()
        instructions = self.ui.instructions.toPlainText()
        if goodsurl == "":
            self.show_error_message("请输入商品链接")
        else:
            product_id = self.extract_id_from_url(goodsurl)
        if goodsname == "":
            self.show_error_message("请输入商品名称")
        elif shopname == "":
            self.show_error_message("请输入店铺名称")
        elif welcome == "":
            self.show_error_message("请输入欢迎语")
        elif instructions == "":
            self.show_error_message("请输入商品说明书")
        else:
            print(goodsurl, goodsname, shopname, welcome, instructions,product_id,"----------------------------------------------")
            try:
                if self.goods:
                    g = self.goods
                    r = self.db.update_goods(g['id'],goodsname,goodsurl,shopname,instructions,welcome,product_id)
                    if r['code'] == 0:
                        self.show_error_message(r['msg'])
                    else:
                        self.show_success_message("修改商品成功")
                        self.goodsAdded.emit()
                        self.close()
                else:
                    r = self.db.add_goods(goodsname,goodsurl,shopname,instructions,welcome,product_id)
                    if r['code'] == 0:
                        self.show_error_message(r['msg'])
                    else:
                        self.show_success_message("添加商品成功")
                        self.goodsAdded.emit()
                        self.clear_input()
                
            except Exception as e:
                print(e)
                self.show_error_message("添加商品失败，请检查填写是否正确")

    def del_goods(self):
        # 弹出确认删除框
        reply = QMessageBox.question(self, "确认删除", f"是否删除商品 {self.goods['product_name']}？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return
        if self.goods:
            self.db.delete_goods(self.goods['id'])
            # self.show_success_message("删除商品成功，请刷新列表")
            self.goodsAdded.emit()
            self.close()

    # 清空输入框，用于添加完成后清空输入框
    def clear_input(self):
        self.ui.goodsurl.clear()
        self.ui.goodsname.clear()
        self.ui.shopname.clear()
        self.ui.welcome.clear()
        self.ui.instructions.clear()

    # 截取连接id
    def extract_id_from_url(self,url):
        # 使用正则表达式匹配URL中的id参数值
        match = re.search(r'id=(\d+)', url)
        if match:
            return match.group(1)  # 返回匹配到的第一个分组，即ID
        else:
            return None  # 如果没有找到匹配，则返回None

    # 初始化信息，用于编辑商品
    def init_info(self,goods):
        self.ui.goodsurl.setText(goods['product_url'])
        self.ui.goodsname.setText(goods['product_name'])
        self.ui.shopname.setText(goods['store_name'])
        self.ui.welcome.setPlainText(goods['welcome_word'])
        self.ui.instructions.setPlainText(goods['details'])

    def show_error_message(self, message):
        # 显示错误消息
        QMessageBox.critical(self, "错误", message)
    
    def show_success_message(self, message):
        # 显示成功消息
        QMessageBox.information(self, "成功", message)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos() # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor)) # 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position) # 更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

