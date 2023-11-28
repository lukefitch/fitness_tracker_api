import pytest
from flask import Flask
from models import db, User

def test_create_user():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    db.init_app(app)

    with app.app_context():
        db.create_all()
        user = User(username='test', email='test@test.com')
        db.session.add(user)
        db.session.commit()

        assert User.query.count() == 1

# Add your other tests here