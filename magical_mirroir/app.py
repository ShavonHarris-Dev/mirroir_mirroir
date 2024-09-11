#define Routes for REST Endpoints

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

messages = []


@app.route('/api/messages', methods=['GET'])
def get_messages():
    return jsonify(messages), 200
 
@app.route('/api/messages', methods=['POST'])
def add_message():
    new_message = request.get_json('message')
    if new_message:
        messages.append(new_message)
        return jsonify({"message": "Message added successfully!"}), 201
    else:
        return jsonify({"error": "No message provided"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)