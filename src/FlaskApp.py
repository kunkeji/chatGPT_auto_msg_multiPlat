import os
import ssl
import threading
from flask import Flask, send_file
from flask_sslify import SSLify
from werkzeug.serving import make_server

class FlaskApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.sslify = SSLify(self.app, permanent=True)
        self.run_dir = os.path.dirname(os.path.abspath(__file__))
        self.hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
        self.cert_file = os.path.join(self.run_dir, "./plugins/server.crt")
        self.key_file = os.path.join(self.run_dir, "./plugins/server.key")
        self.server = None
        self.server_thread = None
        self.should_shutdown = threading.Event()

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
        self.server = make_server('0.0.0.0', 443, self.app, ssl_context=context)

        while not self.should_shutdown.is_set():
            self.server.handle_request()

    def init_message_listener(self):
        self.modify_hosts()
        if not os.path.exists(self.cert_file) or not os.path.exists(self.key_file):
            print("证书文件不存在")
            return False
        self.server_thread = threading.Thread(target=self.start_https_server)
        self.server_thread.start()
        return True

    def run(self):
        if not self.init_message_listener():
            print("消息监听初始化失败")

    def shutdown(self):
        if self.server:
            print("Shutting down the server...")
            self.should_shutdown.set()
            self.server_thread.join()
