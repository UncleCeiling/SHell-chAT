import asyncio
import json
import websockets
from websockets.asyncio.client import connect

# Defaults.
host = "localhost"
port = 54447
server_name = "anon"

# This function handles the connection for the client.
async def chat_handler(uri:str) -> None:
    try:
    # Make the connection.
        async with connect(uri) as websocket:
            # Receive Server name.
            server_name = await websocket.recv()
            print(f"Connected to `{server_name}`.")
            async def receive():
                """Try to handle messages we are receiving."""
                try:
                # Try to receive and print messages.
                    async for message in websocket:
                        print(f"{server_name}@{host} $ {message}",flush=True)
                # But if we can't, just freak out.
                except websockets.ConnectionClosed as e:
                    print("Connection Closed.")
                    return
                except Exception as e:
                    print(f"Exception:\n{e}")
                    return
            async def send():
                """Try to handle any messages we need to send."""
                try:
                    # Take input continuously.
                    while True:
                        message = await asyncio.to_thread(input,f"{server_name}@{host} $ ")
                        # If they want to leave, let them.
                        if message.lower in ["quit","exit"]:
                            print("Closing Client")
                            exit(0)
                        # Otherwise send what they typed.
                        await websocket.send(message)
                # If all else fails, freak out.
                except websockets.ConnectionClosed as e:
                    print("Connection Closed.")
                    return
                except Exception as e:
                    print(f"Exception: \n{e}")
                    return
            # This bit makes sure that send & receive are both running.
            await asyncio.gather(send(),receive())
    # Handle all the potential freakouts by just dumping exceptions.
    except ConnectionRefusedError as e:
        print(f"Connection refused - check settings.\n{e}")
    except ConnectionAbortedError as e:
        print(f"Connection aborted.\n{e}")
    except ConnectionResetError as e:
        print(f"Connection reset.\n{e}")
    except Exception as e:
        print(f"Exception: \n{e}")

# Main loop
if __name__ == "__main__":
    try:
        # Get Configs from file.
        with open("data/client_config.json") as file:
            data = json.load(file)
            host_in,port_in = data["host"],data["port"]
            # Pretend to check if the host in the file is valid.
            if host_in not in [None,""]:
                host = host_in
            else:
                print("Using Default Host.")
            # Actually check if the port is valid.
            if 0 <= port_in <= 65535:
                port = port_in
            else:
                print("Using Default Port.")
    # But if we can't find/read the file, just use defaults.
    except OSError as e:
        print("Couldn't load `client_config.json`. Using Defaults.")
    # Report our intentions.
    print(f"Host: {host}\nPort: {port}")
    # Put the connection info together.
    uri = f"ws://{host}:{port}"
    # Run the connection_handler until it gives up.
    asyncio.run(chat_handler(uri))