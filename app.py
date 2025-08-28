import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for your entire app

with open("responses.json") as file:
    responses = json.load(file)

def chatbot_response(user_input):
    user_input = user_input.lower().strip()
    return responses.get(user_input, "Sorry, I don't understand that yet.")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message')
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    bot_reply = chatbot_response(user_message)
    return jsonify({'response': bot_reply})

if __name__ == "__main__":
    # Running on port 5000 to avoid conflict with your other servers
    app.run(port=5000, debug=True)