from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import jwt, datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@localhost/eventdb'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

@app.route('/')
def home():
    return render_template("login.html")

@app.route('/preferences')
def preferences():
    return render_template("preferences.html")

@app.route('/events')
def events_page():
    return render_template("events.html")

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()

    if user and check_password_hash(user.password, data['password']):
        token = jwt.encode(
            {'user_id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
            app.config['SECRET_KEY']
        )
        return jsonify({'success': True, 'token': token.decode('UTF-8')})
    return jsonify({'success': False, 'message': 'Invalid credentials'})

@app.route('/api/preferences', methods=['POST'])
def save_preferences():
    data = request.json
    # Save user preferences logic
    return jsonify({'success': True, 'message': 'Preferences saved!'})

@app.route('/api/events')
def fetch_events():
    # Example event data
    events = [
        {"name": "Tech Meetup", "location": "NYC", "date": "2024-12-15"},
        {"name": "Music Concert", "location": "NYC", "date": "2024-12-18"},
    ]
    return jsonify(events)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
