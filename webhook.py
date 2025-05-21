from flask import Flask, request, jsonify  # Importing necessary tools

app = Flask(__name__)  # Initialize the Flask app (the web server)

# This is the webhook endpoint
@app.route('/webhook', methods=['POST'])  # Listen only to POST requests at /webhook
def webhook():
    if request.method == 'POST':  # Confirm the method is POST
        data = request.json  # Get the incoming JSON payload from the sender
        print("Received Webhook Data:", data)  # Log it to the console
        return jsonify({"status": "success", "message": "Webhook received!"}), 200
        # Respond with a 200 OK so the sender knows it succeeded

# Start the server if running this file directly
if __name__ == '__main__':
    app.run(port=5000)  # Run the server on port 5000
