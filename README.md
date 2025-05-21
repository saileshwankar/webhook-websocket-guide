
# Webhook and WebSocket Explained with Examples

---

## Table of Contents

1. [Webhook](#webhook)  
2. [WebSocket](#websocket)  
3. [Webhook vs WebSocket](#webhook-vs-websocket)  
4. [Common Errors & Tips](#common-errors--tips)  

---

## 1. Webhook

### What is a Webhook?

A **webhook** is a way for one application to send real-time data to another application via HTTP callbacks. It works on a **push model** — the sender pushes data to your server’s URL endpoint whenever an event occurs.

- Your server exposes a webhook endpoint (a URL).
- The sender (third-party service) POSTs data to this URL.
- Your server processes the data immediately.
- The sender expects a quick HTTP 200 OK response.

### How Webhooks Work?

1. You register your webhook URL with a service.
2. When an event happens, the service calls your webhook URL with event data.
3. Your server receives and processes this data.

### Simple Flask Webhook Example

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # Get JSON payload
    print("Received webhook data:", data)
    # Process the data here
    return jsonify({"status": "success", "message": "Webhook received!"}), 200

if __name__ == '__main__':
    app.run(port=5000)
```

---

## 2. WebSocket

### What is a WebSocket?

A **WebSocket** is a protocol for full-duplex, bidirectional communication between a client (browser) and a server over a single TCP connection.

- Unlike HTTP, WebSockets allow real-time communication in both directions.
- Useful for chat apps, live dashboards, online games, etc.

### How WebSockets Work?

1. Client opens a WebSocket connection to the server.
2. Both keep the connection open.
3. Either side can send messages anytime.
4. Connection stays alive until explicitly closed.

### Python WebSocket Server Example (Using `websockets` Library)

```python
import asyncio
import websockets

async def handler(websocket):
    print("Client connected")
    async for message in websocket:
        print(f"Received: {message}")
        await websocket.send(f"Echo: {message}")

start_server = websockets.serve(handler, "localhost", 6789)

print("WebSocket server running on ws://localhost:6789")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
```

### Browser JavaScript Client Example

Before pasting JS code in your browser console, **type `allow pasting` (without quotes) and press Enter**. Then paste the following:

```javascript
const socket = new WebSocket("ws://localhost:6789");

socket.onopen = () => {
  console.log("Connected to server");
  socket.send("Hello from browser!");
};

socket.onmessage = (event) => {
  console.log("Received:", event.data);
};
```

---

## 3. Webhook vs WebSocket

| Feature             | Webhook                                   | WebSocket                                   |
|---------------------|-------------------------------------------|---------------------------------------------|
| Communication Model | Server to server (push)                    | Full duplex (two-way) real-time communication |
| Protocol            | HTTP POST requests                         | WebSocket protocol (ws:// or wss://)         |
| Connection Type     | Stateless, one-time HTTP request           | Persistent TCP connection                      |
| Use Cases           | Event notifications, data sync, callbacks | Real-time chat, live feeds, gaming, dashboards |
| Client Interaction  | Client does NOT subscribe; sender pushes events | Client connects and maintains open connection |
| Response            | HTTP 200 OK after receiving webhook data | Messages sent asynchronously back and forth  |
| Complexity          | Simple to implement                        | Requires managing open connections and async |
| Security            | HTTPS secure, webhook URL protection       | Secure WebSocket (wss://) for encryption      |

### When to use Webhook?

- For event-driven server-to-server communication.
- When you want simple HTTP callbacks.
- When two-way real-time communication is not needed.

### When to use WebSocket?

- When you need full-duplex real-time communication.
- For chat apps, live notifications, or real-time dashboards.
- When you want to push data instantly without polling.

---

## 4. Common Errors & Tips

### Python WebSocket - “no running event loop” Error

If you see:

```
RuntimeError: no running event loop
```

Use Python 3.7+ with `asyncio.run()` to start your server instead of `get_event_loop()`:

```python
asyncio.run(start_server)
```

### Browser Console Paste Security

When pasting JavaScript in the browser console:

- **Type** `allow pasting` (without quotes) and press Enter **before pasting code**.
- Do **NOT** paste or type quotes around `allow pasting`.
- Don’t wrap it in `console.log(...)`.
- This prevents browser warnings about malicious pasting.

### Content Security Policy (CSP) Errors

If you get errors like:

```
Refused to connect to 'ws://localhost:6789' because it violates Content Security Policy...
```

- Your browser or website blocks insecure WebSocket connections.
- Use secure WebSocket `wss://` or configure CSP to allow `ws://` connections.
- This often happens in environments with strict security policies (e.g., GitHub pages, corporate networks).

---

# Summary

- **Webhooks** are simple HTTP callbacks to receive event data from external services.
- **WebSockets** enable real-time two-way communication between client and server.
- Choose Webhook for simple push notifications, WebSocket for continuous real-time data exchange.
