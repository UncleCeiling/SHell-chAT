# **SH**ell ch**AT** (`sh-at` for short)

> An insecure, un-ergonomic, self-hosted chat app.

## What?

> So many apps tout `Privacy` and `Security` like everyone is carrying around the nuclear football.
> This project (goofy toy?) sets out to prove that communication can be conducted in novel, enjoyable ways.

### 🔓 Insecure

- Well it's a little like `ssh` if you squint, but also it's not secured at all.
- Though I suppose you could argue that that's offset by the fact there's not a real shell attached?

### 🩼 Un-ergonomic

- Users share an input box in real-time.
- Users have no way to tell who is interacting at any given time.
- All messages are ephemeral by nature.
- Sessions do not persist.

### 🏚️ Self-hosted

- No subscriptions.
- No cloud infrastructure.
- Users learn how to port-forward.

## Why?

> Oh erm... I wanted some practice with websockets?  
> Oh and for some reason I really liked the experience of trying to communicate with a friend using only an ssh terminal?  
> So I guess this is my attempt to recreate that experience in a way that is fairly unserious.

## How?

> Well I'll try to comment my code as best as I can, but strategy-wise I'll get back to you on that...

## What\_

### \_have you done so far?

1. Server can receive requests and establish connections.
1. Clients can connect and send messages.
1. Server receives messages and sends to all connections.
1. Clients receive messages and display them properly.
1. Use config file to select host and port for server & client start-up.
1. Make server fetch and display its own public IP.

### \_needs doing?

1. Share server name with clients on join.
1. Share current connections on join and leave.
1. Make user input shared across clients. (May require tkinter and/or a full refactor)

## How do I install it?

> Are you sure?

### 🏤 Server

1. Make sure you have Docker installed.
1. Clone this repo to a folder.
1. Copy/Rename `server_config.json.sample` to `server_config.json`.
1. Either port forward the Default Port - `54447` - or change `server_config.json` to contain a port you do have forwarded.
   - Optionally give your server a name in `server_config.json`.
1. Open the folder in your terminal and run `docker compose up`.
1. Connect via the Client.
1. Profit?

### 💻 Client

1. Make sure you have Python `3.13.5` or higher installed.
1. Clone this repo.
1. Copy/Rename `client_config.json.sample` to `client_config.json`.
1. Make sure the details in `client_config.json` match the public IP and port of the server you want to join.
1. Open a terminal in the folder with `client.py`.
1. Run `pip install -r requirements.txt` in your terminal.
1. Run `client.py`.
1. Chat.
