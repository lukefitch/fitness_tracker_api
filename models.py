from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    type = db.Column(db.String(80), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    intensity = db.Column(db.String(80), nullable=False)
    calories_burned = db.Column(db.Integer, nullable=False)

class DietLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    food_item = db.Column(db.String(80), nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    serving_size = db.Column(db.String(80), nullable=False)

class WorkoutPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    plan_details = db.Column(db.Text, nullable=False)