import asyncio
import json
import websockets
from requests import get
from websockets.asyncio.server import serve

host = "0.0.0.0"
port = 51147

connections = set()

# Handler for each connection
async def message_handler(websocket:websockets.ServerConnection):
    connections.add(websocket) # Register client
    print(f"Client Connected ({len(connections)} total)")
    try:
        # For each message of this connection
        async for message in websocket:
            print(f"Received {message}")# Announce Message
            # Broadcast to everyone
            await asyncio.gather(*[
                connection.send(message) for connection in connections if connection != websocket
            ])
    except websockets.ConnectionClosed as e:
        print(f"Client disconnected")
    finally:
        connections.remove(websocket) # Unregister client

async def server_commands():
    while True:
        try:
            command = await asyncio.to_thread(input,"")
            if command in ["quit","exit"]:
                print("Closing Server")
                exit(0)
        except Exception as e:
            print(f"Exception: \n{e}")

async def main():
    server = await websockets.serve(message_handler,host,port)
    print(f"Server running.")
    await asyncio.gather(
        # server_commands(),
        asyncio.Future())

if __name__ == "__main__":
    # Get Configs from file.
    try:
        with open("data/server_config.json") as file:
            data = json.load(file)
            host_in,port_in = data["host"],data["port"]
            if host_in not in [None,""]:
                host = host_in
            else:
                print("Using Default Host.")
            if 0 <= port_in <= 65535:
                port = port_in
            else:
                print("Using Default Port.")
    except OSError as e:
        print(f"Couldn't load `configs.json`. Using Defaults.\n{e}")
    finally:
        print(f"Host: {host}\nPort: {port}")
    ip = get("https://api.ipify.org").text
    if ip != host:
        print(f"Public IP: {ip}")
    asyncio.run(main())