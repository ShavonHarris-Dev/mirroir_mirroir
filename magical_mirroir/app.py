#define Routes for REST Endpoints

from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.secret_key = 'secretkey'
CORS(app)

#login manager setup initializes and specifies the login view to redirect unauthenticated users
login_manager = LoginManager() #handles login sessions for the user
login_manager.init_app(app) #connects login manager to flask app
login_manager.login_view = 'login' #tells the flask login where to redirect users who are not logged in

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) #returns the user object from the database. Tells flask login how to load user from the database using their user_id


messages = [
     {"message": "You are doing amazing! Keep going."},
    {"message": "Don't forget, you're loved and appreciated."}
]

# User class for login
# represents the users of the application
# User model (define this first)
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)

# Friend model (define after User)
class Friend(db.Model):
    __tablename__ = 'friends'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    friend_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    status = db.Column(db.String(50), default='pending')
    user = db.relationship('User', foreign_keys=[user_id], backref='friends')
    friend = db.relationship('User', foreign_keys=[friend_id])

# Messages model (define after User)
class Messages(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    sender = db.relationship('User', foreign_keys=[sender_id], backref='sent_messages')
    recipient = db.relationship('User', foreign_keys=[recipient_id], backref='received_messages')

  
db.ForeignKey('users.id')

  #create the database tables
with app.app_context():
    db.create_all()



# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/messages', methods=['GET'])
@cross_origin()
def get_messages():
    return jsonify(messages),200
 
# @app.route('/api/new_message', methods=['POST'])
# def add_message():
#     # Fetch the new message from the request
#     data = request.get_json()
#     new_message = data.get('message')

#     if new_message:
#         # Add the new message to the list of messages
#         messages.append({"message": new_message})
#         return jsonify({"message": "Message added successfully!"}), 201
#     else:
#         return jsonify({"error": "No message provided"}), 400

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    sender_id = data.get('sender_id')
    recipient_id = data.get('recipient_id')
    content = data.get('content')

    if not sender_id or not recipient_id or not content:
        return jsonify({'error': 'Missing data'}), 400

    sender = User.query.get(sender_id)
    recipient = User.query.get(recipient_id)

    if not sender or not recipient:
        return jsonify({'error': 'User not found'}), 404

    message = Messages(sender_id=sender_id, recipient_id=recipient_id, content=content)
    db.session.add(message)
    db.session.commit()

    return jsonify({'message': 'Message sent successfully!'}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)