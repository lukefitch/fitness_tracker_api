from flask import Flask, request, jsonify
from models import db, User, Activity, DietLog, WorkoutPlan

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/fitness_tracker_db'
db.init_app(app)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data['username']
    email = data['email']
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created'}), 201

# Add your other routes here

if __name__ == '__main__':
    app.run(debug=True)