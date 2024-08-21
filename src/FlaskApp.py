import os
import ssl
from flask import Flask, send_file
from flask_sslify import SSLify
from threading import Lock, Thread
import time

class FlaskApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.sslify = SSLify(self.app, permanent=True)
        self.run_dir = os.path.dirname(os.path.abspath(__file__))
        self.hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
        self.cert_file = os.path.join(self.run_dir, "./plugins/server.crt")
        self.key_file = os.path.join(self.run_dir, "./plugins/server.key")

        self.add_routes()

    def add_routes(self):
        @self.app.route("/imsupport")
        def inject_js():
            js_resource_path = os.path.join(self.run_dir, "./plugins/kelin.js")
            return send_file(js_resource_path, mimetype='application/javascript')

    def modify_hosts(self):
        with open(self.hosts_path, 'r+', encoding='utf-8') as file:
            hosts_content = file.read()
            new_entry = "127.0.0.1 iseiya.taobao.com\n"
            if new_entry not in hosts_content:
                file.seek(0, 2)
                file.write(new_entry)

    def start_https_server(self):
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile=self.cert_file, keyfile=self.key_file)
        try:
            self.http_thread = Thread(target=lambda: self.app.run(port=443, ssl_context=context))
            self.http_thread.start()
            print('服务启动成功')
            return True
        except Exception as e:
            print(f"服务启动失败: {e}")
            return False

    def init_message_listener(self):
        with Lock():
            self.modify_hosts()
            if not os.path.exists(self.cert_file) or not os.path.exists(self.key_file):
                print("证书文件不存在")
                return False
            return self.start_https_server()

    def run(self):
        if not self.init_message_listener():
            print("消息监听初始化失败")
        else:
            while True:
                time.sleep(1)