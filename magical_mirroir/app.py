#define Routes for REST Endpoints

from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'secretkey'
CORS(app)

login_manager = LoginManager #handles login sessions for the user
login_manager.init_app(app) #connects login manager to flask app
login_manager.login_view = 'login' #tells the flask login where to redirect users who are not logged in

messages = [
     {"message": "You are doing amazing! Keep going."},
    {"message": "Don't forget, you're loved and appreciated."}
]

# User class for login
class User(UserMixin):
    def __init_(self, id):
        self.id = id

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