from PySide6.QtCore import Qt, QUrl, Signal
from PySide6.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout, QPushButton, QToolBar, QLineEdit, QPlainTextEdit, QSplitter
from PySide6.QtGui import QAction
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineProfile, QWebEnginePage, QWebEngineSettings
import logging
import datetime
import json
class CustomWebPage(QWebEnginePage):
    """自定义网页，用于捕获控制台消息"""
    console_message_received = Signal(str)  # 定义信号

    def javaScriptConsoleMessage(self, level, message, line_number, source_id):
        """重写控制台消息处理方法"""
        try:
            # 检查是否是 titan 消息
            if "titan" in message:
                try:
                    # 提取完整的 JSON 对象
                    import re
                    json_match = re.search(r'%ctitan[^{]*(\{[\s\S]*\})', message)
                    
                    if json_match:
                        json_str = json_match.group(1)
                        data = json.loads(json_str)
                        
                        if "message" in data:
                            msg = data["message"]
                            if msg.get("from", {}).get("role") == "user":
                                # 格式化输出消息
                                formatted_message = "\n" + "=" * 50 + "\n"
                                formatted_message += f"用户ID: {msg['from'].get('uid', 'Unknown')}\n"
                                formatted_message += f"用户昵称: {msg.get('nickname', '')}\n"
                                formatted_message += f"消息内容: {msg.get('content', '')}\n"
                                formatted_message += f"消息ID: {msg.get('msg_id', '')}\n"
                                formatted_message += f"时间戳: {msg.get('ts', '')}\n"
                                formatted_message += "=" * 50
                                self.console_message_received.emit(formatted_message)
                                
                                # 自动回复消息
                                user_id = msg['from'].get('uid')
                                content = msg.get('content', '')
                                self.auto_reply_to_user(user_id, content)
                except Exception as e:
                    print(f"JSON提取错误: {str(e)}")
        except Exception as e:
            print(f"消息处理错误: {str(e)}")

    def auto_reply_to_user(self, user_id, content):
        """自动回复用户消息"""
        script = f"""
        (function() {{
            function simulateMouseEvent(element, eventType) {{
                const event = new MouseEvent(eventType, {{
                    view: window,
                    bubbles: true,
                    cancelable: true,
                    clientX: 1,
                    clientY: 1,
                    buttons: 1
                }});
                element.dispatchEvent(event);
            }}

            function simulateClick(element) {{
                element.focus();
                simulateMouseEvent(element, 'mousedown');
                simulateMouseEvent(element, 'mouseup');
                simulateMouseEvent(element, 'click');
            }}

            function simulateInputEvents(element, value) {{
                // 清空现有内容
                element.value = '';
                element.focus();
                
                // 模拟逐字输入
                const text = value;
                for (let i = 0; i < text.length; i++) {{
                    element.value += text[i];
                    
                    // 触发输入事件
                    element.dispatchEvent(new Event('input', {{ bubbles: true }}));
                    element.dispatchEvent(new Event('change', {{ bubbles: true }}));
                    
                    // 触发键盘事件
                    const keyCode = text.charCodeAt(i);
                    const keyEvents = [
                        new KeyboardEvent('keydown', {{ key: text[i], keyCode: keyCode, bubbles: true }}),
                        new KeyboardEvent('keypress', {{ key: text[i], keyCode: keyCode, bubbles: true }}),
                        new KeyboardEvent('keyup', {{ key: text[i], keyCode: keyCode, bubbles: true }})
                    ];
                    keyEvents.forEach(event => element.dispatchEvent(event));
                }}
            }}

            // 1. 找到并点击用户的聊天框
            function findChatItem() {{
                // 尝试所有可能的后缀
                const suffixes = ['-0-unTimeout', '-0-all', '-1-all'];
                let chatItem = null;
                
                for (const suffix of suffixes) {{
                    const selector = `[data-random="{user_id}${{suffix}}"]`;
                    chatItem = document.querySelector(selector);
                    if (chatItem) {{
                        console.log('找到聊天框，使用选择器:', selector);
                        break;
                    }}
                }}
                return chatItem;
            }}

            const chatItem = findChatItem();
            console.log('找到聊天框:', chatItem);
            
            if (chatItem) {{
                console.log('正在点击聊天框');
                simulateClick(chatItem);
                
                // 2. 等待DOM更新后设置输入框内容并点击发送
                setTimeout(() => {{
                    const textarea = document.getElementById('replyTextarea');
                    const sendBtn = document.querySelector('.send-btn');
                    console.log('输入框:', textarea);
                    console.log('发送按钮:', sendBtn);
                    
                    if (textarea && sendBtn) {{
                        console.log('正在设置输入框内容:', {json.dumps(content)});
                        
                        // 模拟输入事件
                        simulateInputEvents(textarea, {json.dumps(content)});
                        
                        // 等待一段时间后点击发送按钮
                        setTimeout(() => {{
                            console.log('正在点击发送按钮');
                            // 检查按钮状态
                            const buttonDisabled = sendBtn.disabled || sendBtn.classList.contains('disabled');
                            console.log('按钮状态:', {{ disabled: buttonDisabled }});
                            
                            if (!buttonDisabled) {{
                                // 尝试多种方式触发按钮点击
                                simulateClick(sendBtn);
                                sendBtn.click();
                                
                                // 如果按钮有原生点击处理器，尝试直接调用
                                const clickEvent = new MouseEvent('click', {{
                                    bubbles: true,
                                    cancelable: true,
                                    view: window
                                }});
                                sendBtn.dispatchEvent(clickEvent);
                                
                                console.log('消息已发送');
                            }} else {{
                                console.error('发送按钮被禁用');
                                // 输出更多按钮信息以便调试
                                console.log('按钮类名:', sendBtn.className);
                                console.log('按钮样式:', window.getComputedStyle(sendBtn));
                            }}
                        }}, 800);  // 增加等待时间到800ms
                    }} else {{
                        console.error('找不到输入框或发送按钮');
                        console.log('textarea:', document.getElementById('replyTextarea'));
                        console.log('send-btn:', document.querySelector('.send-btn'));
                        // 输出整个文档结构以便调试
                        console.log('document body:', document.body.innerHTML);
                    }}
                }}, 1000);  // 等待1000ms确保DOM已更新
            }} else {{
                console.error('找不到用户聊天框');
                console.log('用户ID:', "{user_id}");
                console.log('所有可能的聊天框:', document.querySelectorAll('[data-random]'));
            }}
        }})();
        """
        self.runJavaScriptAndLog(script)

    def runJavaScriptAndLog(self, script):
        """运行 JavaScript 并记录结果"""
        def callback(result):
            if result:
                try:
                    if isinstance(result, str):
                        self.console_message_received.emit(result)
                    else:
                        self.console_message_received.emit(json.dumps(result, indent=2))
                except:
                    self.console_message_received.emit(str(result))
        
        self.runJavaScript(script, callback)

class ConsoleWidget(QPlainTextEdit):
    """控制台窗口组件"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setReadOnly(True)
        self.setMaximumHeight(200)
        self.setStyleSheet("""
            QPlainTextEdit {
                background-color: #1e1e1e;
                color: #ffffff;
                font-family: Consolas, Monaco, monospace;
                font-size: 12px;
                padding: 5px;
            }
        """)

    def append_message(self, message):
        """添加消息到控制台"""
        self.appendPlainText(message)
        # 滚动到底部
        self.verticalScrollBar().setValue(self.verticalScrollBar().maximum())

class BrowserTab(QWidget):
    def __init__(self, url, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)  # 设置布局边距为0
        
        # 创建独立的 QWebEngineProfile
        self.profile = QWebEngineProfile(self)
        self.profile.setHttpCacheType(QWebEngineProfile.MemoryHttpCache)
        self.profile.setPersistentCookiesPolicy(QWebEngineProfile.NoPersistentCookies)
        
        # 启用本地存储
        self.profile.setPersistentStoragePath("./browser_data")
        self.profile.settings().setAttribute(
            QWebEngineSettings.WebAttribute.LocalStorageEnabled, True
        )
        
        # 创建工具栏
        toolbar = QToolBar()
        self.layout.addWidget(toolbar)  # 将工具栏添加到布局中
        
        # 添加刷新按钮
        self.refresh_button = QPushButton("刷新", self)
        self.refresh_button.clicked.connect(self.refresh_page)
        toolbar.addWidget(self.refresh_button)
        
        # 添加地址栏
        self.url_edit = QLineEdit(self)
        self.url_edit.returnPressed.connect(self.load_url)
        toolbar.addWidget(self.url_edit)
        
        # 添加开发者工具按钮
        dev_tools_action = QAction("开发者工具", self)
        dev_tools_action.setCheckable(True)
        dev_tools_action.triggered.connect(self.toggle_dev_tools)
        toolbar.addAction(dev_tools_action)
        
        # 创建水平分割布局
        splitter = QSplitter(Qt.Vertical)
        self.layout.addWidget(splitter)
        
        # 创建网页视图
        self.web_view = QWebEngineView()
        self.page = CustomWebPage(self.profile, self.web_view)
        self.web_view.setPage(self.page)
        splitter.addWidget(self.web_view)
        
        # 创建开发者工具视图
        self.dev_tools = QWebEngineView()
        self.page.setDevToolsPage(self.dev_tools.page())
        splitter.addWidget(self.dev_tools)
        self.dev_tools.hide()  # 默认隐藏开发者工具
        
        # 创建控制台输出窗口
        self.console_widget = ConsoleWidget(self)
        self.layout.addWidget(self.console_widget)
        
        # 连接控制台消息信号
        self.page.console_message_received.connect(self.console_widget.append_message)
        
        # 配置安全设置
        settings = self.page.settings()
        settings.setAttribute(QWebEngineSettings.WebAttribute.AllowRunningInsecureContent, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.AllowGeolocationOnInsecureOrigins, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.LocalStorageEnabled, True)
        self.profile.setHttpAcceptLanguage("zh-CN,zh;q=0.9")
        self.page.setBackgroundColor(Qt.white)
        
        # 连接URL变化信号
        self.web_view.urlChanged.connect(self.url_changed)
        
        # 加载URL
        self.load_url(url)
        
        # 连接页面加载完成信号
        self.web_view.loadFinished.connect(self.on_load_finished)
    
    def refresh_page(self):
        """刷新当前页面"""
        self.web_view.reload()
    
    def load_url(self, url):
        """加载URL"""
        if isinstance(url, str):
            qurl = QUrl(url)
        else:
            qurl = QUrl(self.url_edit.text())
        if qurl.scheme() == "":
            qurl.setScheme("https")
        self.web_view.load(qurl)
    
    def url_changed(self, url):
        """URL变化时更新地址栏"""
        self.url_edit.setText(url.toString())
    
    def on_load_finished(self, ok):
        """页面加载完成后的处理"""
        if ok:
            # 注入调试标志
            debug_script = """
            localStorage.setItem('__debug__', 'true');
            window.__debug__ = true;

            // 重写 console.log 等方法来更好地处理对象
            (function() {
                function stringify(obj) {
                    try {
                        return JSON.stringify(obj, function(key, value) {
                            if (value instanceof Error) {
                                var error = {};
                                Object.getOwnPropertyNames(value).forEach(function(key) {
                                    error[key] = value[key];
                                });
                                return error;
                            }
                            if (typeof value === 'function') {
                                return value.toString();
                            }
                            if (value instanceof Element) {
                                return value.outerHTML;
                            }
                            return value;
                        }, 2);
                    } catch (e) {
                        return String(obj);
                    }
                }

                var originalConsole = {
                    log: console.log,
                    error: console.error,
                    warn: console.warn,
                    info: console.info
                };

                function wrap(method) {
                    return function() {
                        var args = Array.prototype.slice.call(arguments).map(function(arg) {
                            return typeof arg === 'object' ? stringify(arg) : String(arg);
                        });
                        originalConsole[method].apply(console, args);
                    };
                }

                console.log = wrap('log');
                console.error = wrap('error');
                console.warn = wrap('warn');
                console.info = wrap('info');
            })();

            // 添加错误处理
            window.onerror = function(message, source, lineno, colno, error) {
                console.error({
                    message: message,
                    source: source,
                    line: lineno,
                    column: colno,
                    error: error
                });
                return false;
            };

            // 添加未处理的 Promise 拒绝处理
            window.onunhandledrejection = function(event) {
                console.error('Unhandled Promise Rejection:', event.reason);
            };
            """
            self.page.runJavaScript(debug_script)
            
            # 处理混合内容警告
            warning_script = """
            console.warn = (function(old) {
                return function() {
                    if (arguments[0].indexOf('Mixed Content') === -1) {
                        old.apply(this, arguments);
                    }
                }
            })(console.warn);
            """
            self.page.runJavaScript(warning_script)

    def toggle_dev_tools(self, checked):
        """切换开发者工具的显示状态"""
        if checked:
            self.dev_tools.show()
        else:
            self.dev_tools.hide()

    def keyPressEvent(self, event):
        """处理按键事件"""
        # 按下 F12 时切换开发者工具
        if event.key() == Qt.Key_F12:
            action = self.findChild(QAction, "开发者工具")
            if action:
                action.trigger()
        else:
            super().keyPressEvent(event)

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("拼多多客服")
        self.resize(1200, 800)
        
        # 创建工具栏
        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)
        
        # 添加新标签页按钮
        self.new_tab_button = QPushButton("+", self)
        self.new_tab_button.clicked.connect(self.add_new_tab)
        self.toolbar.addWidget(self.new_tab_button)
        
        # 添加开发者工具切换按钮
        # self.toggle_devtools_button = QPushButton("开发者工具", self)
        # self.toggle_devtools_button.setCheckable(True)
        # self.toggle_devtools_button.setChecked(True)
        # self.toggle_devtools_button.clicked.connect(self.toggle_devtools)
        # self.toolbar.addWidget(self.toggle_devtools_button)
        
        # 创建标签页容器
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.setCentralWidget(self.tabs)
        
        # 添加第一个标签页
        self.add_new_tab()
    
    def add_new_tab(self):
        """添加新标签页"""
        url = "https://mms.pinduoduo.com/chat-merchant/index.html?debug=true#/"
        new_tab = BrowserTab(url)
        index = self.tabs.addTab(new_tab, f"拼多多客服 {self.tabs.count() + 1}")
        self.tabs.setCurrentIndex(index)
    
    # def toggle_devtools(self):
    #     """切换开发者工具显示/隐藏"""
    #     current_tab = self.tabs.currentWidget()
    #     if current_tab:
    #         if self.toggle_devtools_button.isChecked():
    #             current_tab.dev_tools.show()
    #         else:
    #             current_tab.dev_tools.hide()
    
    def close_tab(self, index):
        """关闭标签页"""
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)
        else:
            self.close()
    
    def closeEvent(self, event):
        """关闭窗口时清理资源"""
        for i in range(self.tabs.count()):
            tab = self.tabs.widget(i)
            tab.web_view.page().profile().deleteLater()
            tab.web_view.page().deleteLater()
            tab.web_view.deleteLater()
            tab.dev_tools.deleteLater()
        super().closeEvent(event)