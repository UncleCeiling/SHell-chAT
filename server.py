import asyncio
import json
import websockets
from requests import get
from websockets.asyncio.server import serve

# Defaults
host = "0.0.0.0"
port = 54447
server_name = "anon"
connections = set()

# Handler for each connection.
async def message_handler(websocket:websockets.ServerConnection):
    # Register client.
    connections.add(websocket) 
    print(f"Client Connected ({len(connections)} total)")
    try:
        # Send them the server name.
        await websocket.send(server_name)
        # For each message of this connection.
        async for message in websocket:
            print(f"Received {message}")
            # Broadcast to everyone except the sender.
            await asyncio.gather(*[
                connection.send(message) for connection in connections if connection != websocket
            ])
    # Handle Connection losses.
    except websockets.ConnectionClosed as e:
        print(f"Client disconnected")
    # Unregister client.
    finally:
        connections.remove(websocket)
        print(f"Client Unregistered ({len(connections)} left)")

# UNUSED
# async def server_commands():
#     while True:
#         try:
#             command = await asyncio.to_thread(input,"")
#             if command in ["quit","exit"]:
#                 print("Closing Server")
#                 exit(0)
#         except Exception as e:
#             print(f"Exception: \n{e}")

async def main():
    # Instantiate the main server object.
    server = await websockets.serve(message_handler,host,port)
    print(f"Server running.")
    # Make it so the asyncio loop never stops.
    await asyncio.gather(
        # server_commands(), # UNUSED
        asyncio.Future())

if __name__ == "__main__":
    try:
        # Get Configs from file.
        with open("data/server_config.json") as file:
            data = json.load(file)
            host_in,port_in,name_in = data["host"],data["port"],data["name"]
            # Pretend we are validating the host.
            if host_in not in [None,""]:
                host = host_in
            else:
                print("Using Default Host.")
            # Actually validate the port .
            if 0 <= port_in <= 65535:
                port = port_in
            else:
                print("Using Default Port.")
            if name_in not in [None,""]:
                server_name = name_in
            print(f"Server Name: `{server_name}`")
    # Fall back on Defaults if we can't find/read the config file  
    except OSError as e:
        print(f"Couldn't load `server_config.json`. Using Defaults.\n{e}")
    finally:
        print(f"Host: {host}\nPort: {port}")
    # Fetch and announce the public IP
    ip = get("https://api.ipify.org").text
    if ip != host:
        print(f"Public IP: {ip}")
    # Leave to simmer until negative consequences come knocking.
    asyncio.run(main())