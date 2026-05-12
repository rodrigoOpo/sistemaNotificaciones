from fastapi import WebSocket


class ClientManager:
    def __init__(self):
        self.connected_clients = []


    async def connect(self, ws: WebSocket):
        print(f"client {ws.client.host}:{ws.client.port}")
        self.connected_clients.append(ws)
        print(f"connected clients:{self.connected_clients}")


    async def send_message(self, ws: WebSocket, message: str):
        message={
            "client": f"{ws.client.host}:{ws.client.port}",
            "message": message
        }
        await ws.send_json(message)



    async def disconnect(self, websocket):
        self.connected_clients.remove(websocket)
        print(f"client {websocket.client.host}:{websocket.client.port} is disconnected")
        print(f"connected clients {self.connected_clients}")


