# **SH**ell ch**AT** (`shat` for short)

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

## What...

### ...have you done so far?

1. Server can receive requests and establish connections.
1. Clients can connect and send messages.
1. Server receives messages and sends to all connections.
1. Clients receive messages and display them properly.
1. Use config file to select host and port for server & client start-up.
1. Make server fetch and display its own public IP.

### ...needs doing?

1. Make user input shared across clients. (May require tkinter and/or a full refactor)
