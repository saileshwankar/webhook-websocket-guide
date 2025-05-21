# WebSocket Communication Using Python and JavaScript

## 📌 Overview

This guide demonstrates how to set up a simple WebSocket server in Python using the `websockets` library and connect to it using a JavaScript client from the browser console.

---

## 🧱 Requirements

* Python 3.7+
* `websockets` library (install via pip)
* Modern web browser (for client-side JavaScript)

---

## 📦 Install Dependencies

Open your terminal or PowerShell:

```bash
pip install websockets
```

If using a virtual environment (recommended):

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install websockets
```

---

## 🖥️ WebSocket Server (Python)

Create a file named `websocket_server.py` with the following code:

```python
import asyncio
import websockets

async def handler(websocket):
    print("🔌 Client connected")
    async for message in websocket:
        print(f"📨 Received from client: {message}")
        reply = f"Echo: {message}"
        await websocket.send(reply)

async def main():
    async with websockets.serve(handler, "localhost", 6789):
        print("🚀 WebSocket server running on ws://localhost:6789")
        await asyncio.Future()  # run forever

if __name__ == '__main__':
    asyncio.run(main())
```

Then run it:

```bash
python websocket_server.py
```

---

## 🌐 WebSocket Client (Browser JavaScript)

Open your browser **Developer Tools Console** and paste the following code:

```javascript
const socket = new WebSocket("ws://localhost:6789");

socket.onopen = () => {
  console.log("✅ Connected to server");
  socket.send("Hello from browser!");
};

socket.onmessage = (event) => {
  console.log("📨 Received:", event.data);
};
```

**⚠️ Note:** In Chrome, if you see a message like:

```
Warning: Don’t paste code into the DevTools Console that you don’t understand...
```

Type `allow pasting` (without quotes) manually to enable pasting.

---

## 🧪 Example Output

On the server terminal:

```
🔌 Client connected
📨 Received from client: Hello from browser!
```

In the browser console:

```
✅ Connected to server
📨 Received: Echo: Hello from browser!
```

---

## 🛠️ Troubleshooting

* **`ModuleNotFoundError: No module named 'websockets'`**

  * Activate your virtual environment or reinstall using `pip install websockets`

* **`RuntimeError: no running event loop`**

  * Ensure you're using `asyncio.run(main())` instead of deprecated loop usage

* **Content Security Policy (CSP) Errors in Hosted Pages (e.g. ChatGPT)**

  * You cannot run WebSocket JS code on websites that block external WS connections due to security policies.
  * Instead, run it from your **local HTML page** or in DevTools on a localhost-served site.

---

## ✅ Summary

This example shows a minimal WebSocket server in Python and how to test it using browser JavaScript. It's useful for:

* Real-time chat
* Notifications
* Live updates in dashboards

---

## 🔗 Related Tools

* [websockets Python Docs](https://websockets.readthedocs.io/)
* [MDN WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)

---

Made with ❤️ for learning real-time communication!
