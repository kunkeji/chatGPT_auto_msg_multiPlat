from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading

def run_test_server(port=8000):
    """运行一个简单的HTTP服务器来处理静态文件请求"""
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Starting test server on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run_test_server()