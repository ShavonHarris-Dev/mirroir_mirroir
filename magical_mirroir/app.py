#define Routes for REST Endpoints

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

messages = [
     {"message": "You are doing amazing! Keep going."},
    {"message": "Don't forget, you're loved and appreciated."}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/messages', methods=['GET'])
@cross_origin()
def get_messages():
    return jsonify(messages),200
 
@app.route('/api/new_message', methods=['POST'])
def add_message():
    # Fetch the new message from the request
    data = request.get_json()
    new_message = data.get('message')

    if new_message:
        # Add the new message to the list of messages
        messages.append({"message": new_message})
        return jsonify({"message": "Message added successfully!"}), 201
    else:
        return jsonify({"error": "No message provided"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)