import asyncio
import json
import websockets
from websockets.asyncio.client import connect

host = "localhost"
port = 51147
shared_text = str()
# This function handles the connection for the client
async def chat_handler(uri:str) -> None:
    try:
    # Make the connection
        async with connect(uri) as websocket:
            print("Connected.")
            async def receive():
                try:
                    async for message in websocket:
                        if message[-1] == "\n":
                            print(f"{host}:{port} $ {message[0:-1]}",flush=True)
                        else:
                            pass
                except websockets.ConnectionClosed as e:
                    print("Connection Closed.")
                    return
                except Exception as e:
                    print(f"Exception:\n{e}")
                    return
            async def send():
                try:
                    while True:
                        # print(f"{host}:{port} $ ",end="",flush=True)
                        message = await asyncio.to_thread(input,f"{host}:{port} $ ")
                        if message.lower in ["quit","exit"]:
                            print("Closing Client")
                            exit(0)
                        await websocket.send(message)
                except websockets.ConnectionClosed as e:
                    print("Connection Closed.")
                    return
                except Exception as e:
                    print(f"Exception: \n{e}")
                    return
            await asyncio.gather(send(),receive())
    except ConnectionRefusedError as e:
        print(f"Connection refused - check settings.\n{e}")
    except ConnectionAbortedError as e:
        print("Connection aborted.")
    except ConnectionResetError as e:
        print("Connection reset.")
    except Exception as e:
        print(f"Exception: \n{e}")

# Main loop
if __name__ == "__main__":# Get Configs from file.
    try:
        with open("data/client_config.json") as file:
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
        print("Couldn't load `configs.json`. Using Defaults.")
    print(f"Host: {host}\nPort: {port}")
    uri = f"ws://{host}:{port}"
    # Run the connection_handler until it completes
    asyncio.run(chat_handler(uri))