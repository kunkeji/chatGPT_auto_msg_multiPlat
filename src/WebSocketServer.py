import threading
import asyncio
import websockets
from websockets import WebSocketServerProtocol
from PySide6.QtCore import QCoreApplication
import uuid
import json

class WebSocketServer:
    def __init__(self,dispatcher, ui,host='localhost', port=8765):
        self.host = host
        self.port = port
        self.clients = {}
        self.dispatcher = dispatcher
        self.loop = None
        self.server_thread = None
        self.server = None
        self.should_shutdown = threading.Event()
        self.ui = ui

    async def register(self, websocket: WebSocketServerProtocol):
        client_id = str(uuid.uuid4())  # Generate a unique ID for the client
        self.clients[client_id] = websocket
        self.ui.textEdit.append(f"连接成功")
        self.ui.qianniu_state.setText(f"已连接")
        self.ui.pushButton_2.hide()
        return client_id

    async def unregister(self, client_id: str):
        websocket = self.clients.pop(client_id, None)
        if websocket:
            self.ui.textEdit.append(f"已断开")
            print(f"终端断开: {client_id} - {websocket.remote_address}")
            self.ui.qianniu_state.setText(f"未连接")
            self.ui.pushButton_2.show()

    async def send_message_to_client(self, client_id: str, message: str):
        websocket = self.clients.get(client_id)
        if websocket:
            await websocket.send(message)
            print(f"消息发送到 {client_id}: {message}")
        else:
            print(f"终端ID {client_id} 不存在")

    async def send_message_to_all(self, message: str):
        if self.clients:
            await asyncio.gather(*(client.send(message) for client in self.clients.values()))
            print(f"消息已发送给所有客户端: {message}")

    async def handle_connection(self, websocket: WebSocketServerProtocol):
        client_id = await self.register(websocket)
        try:
            async for message in websocket:
                massagedata = {
                    'client_id':client_id,
                    'message': message
                }
                self.dispatcher.message_received.emit(json.dumps(massagedata))
                # print(f"收到消息来自的 {client_id}: {message}")
        finally:
            await self.unregister(client_id)

    async def start_server(self):
        try:
            self.server = await websockets.serve(self.handle_connection, self.host, self.port)
            print("websockets启动成功")
            await self.server.wait_closed()
        except Exception as e:
            print(f"WebSocket服务器错误: {e}")

    def run(self):
        try:
            self.loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self.loop)
            self.loop.run_until_complete(self.start_server())
            self.loop.run_forever()
        except Exception as e:
            print(f"运行错误: {e}")
        finally:
            if not self.loop.is_closed():
                self.loop.close()

    async def close_connections(self):
        # 关闭所有客户端连接
        for client_id, websocket in list(self.clients.items()):
            try:
                await websocket.close()
                await self.unregister(client_id)
            except:
                pass

    def stop_server(self):
        if self.server is None:
            return
            
        async def cleanup():
            await self.close_connections()
            self.server.close()
            await self.server.wait_closed()

        if self.loop and self.loop.is_running():
            future = asyncio.run_coroutine_threadsafe(cleanup(), self.loop)
            future.result(timeout=5)  # 等待清理完成，最多5秒
            self.loop.call_soon_threadsafe(self.loop.stop)

        if self.server_thread and self.server_thread.is_alive():
            self.server_thread.join(timeout=5)  # 等待线程结束，最多5秒

        print("WebSocketServer 已关闭")

    def start(self):
        self.server_thread = threading.Thread(target=self.run)
        self.server_thread.start()

    def send_message(self, client_id: str, message: str):
        if client_id:
            asyncio.run_coroutine_threadsafe(self.send_message_to_client(client_id, message), self.loop).result()
        else:
            asyncio.run_coroutine_threadsafe(self.send_message_to_all(message), self.loop).result()
        
