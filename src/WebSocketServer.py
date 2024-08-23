import threading
import asyncio
import websockets
from websockets import WebSocketServerProtocol
from PyQt6.QtCore import QCoreApplication
import uuid
import json

class WebSocketServer:
    def __init__(self,dispatcher, host='localhost', port=8765):
        self.host = host
        self.port = port
        self.clients = {}
        self.dispatcher = dispatcher
        self.loop = asyncio.new_event_loop()
        self.server_thread = threading.Thread(target=self.start_server, args=(self.loop,))
        self.should_shutdown = threading.Event()



    async def register(self, websocket: WebSocketServerProtocol):
        client_id = str(uuid.uuid4())  # Generate a unique ID for the client
        self.clients[client_id] = websocket
        print(f"终端接入: {client_id} - {websocket.remote_address}")
        return client_id

    async def unregister(self, client_id: str):
        websocket = self.clients.pop(client_id, None)
        if websocket:
            print(f"终端断开: {client_id} - {websocket.remote_address}")

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

    async def handle_connection(self, websocket: WebSocketServerProtocol, path: str):
        client_id = await self.register(websocket)
        try:
            async for message in websocket:
                massagedata = {
                    'client_id':client_id,
                    'message': message
                }
                if isinstance(massagedata, dict):
                    # 将 dict 转换为 JSON 字符串
                    massagedata = json.dumps(massagedata)
                else:
                    massagedata = massagedata
                    
                self.dispatcher.message_received.emit(massagedata)
                # print(f"收到消息来自的 {client_id}: {message}")
        finally:
            await self.unregister(client_id)



    def start_server(self, loop):
        asyncio.set_event_loop(loop)
        start_server = websockets.serve(self.handle_connection, self.host, self.port)
        loop.run_until_complete(start_server)

        # Run the event loop until stopped
        while not self.should_shutdown.is_set():
            try:
                loop.run_forever()
            except RuntimeError:
                # Handle the case where the loop is stopped
                break

    def run(self):
        self.server_thread.start()

    def send_message(self, client_id: str, message: str):
        if client_id:
            asyncio.run_coroutine_threadsafe(self.send_message_to_client(client_id, message), self.loop).result()
        else:
            asyncio.run_coroutine_threadsafe(self.send_message_to_all(message), self.loop).result()

    def stop_server(self):
        self.should_shutdown.set()
        self.loop.call_soon_threadsafe(self.loop.stop)
        self.server_thread.join()
