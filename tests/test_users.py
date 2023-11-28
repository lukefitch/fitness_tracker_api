import pytest
from app import create_app
from models import db, User

@pytest.fixture(scope='module')
def test_client():
    # Setup Flask test client
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'})
    testing_client = app.test_client()

    # Establish an application context before running the tests
    with app.app_context():
        db.init_app(app)
        db.create_all()

    yield testing_client  # this is where the testing happens!

    # Teardown after tests are completed
    with app.app_context():
        db.session.remove()
        db.drop_all()

def test_create_user(test_client):
    # Test creating a new user
    response = test_client.post('/users', json={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'strong_password'
    })
    assert response.status_code == 201
    assert 'User created' in response.get_json()['message']

def test_register(test_client):
    # Test user registration
    response = test_client.post('/register', json={
        'username': 'testuser2',
        'email': 'testuser2@example.com',
        'password': 'another_strong_password'
    })
    assert response.status_code == 201
    assert 'User registered' in response.get_json()['message']

def test_login(test_client):
    # First create a user to login
    test_client.post('/users', json={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'strong_password'
    })
    # Test logging in with the new user
    response = test_client.post('/login', json={
        'username': 'testuser',
        'password': 'strong_password'
    })
    assert response.status_code == 200
    assert 'access_token' in response.get_json()

def test_logout(test_client):
    # Create a user and login to obtain a token
    test_client.post('/users', json={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'strong_password'
    })
    login_response = test_client.post('/login', json={
        'username': 'testuser',
        'password': 'strong_password'
    })
    token = login_response.get_json()['access_token']

    # Test logging out with the token
    headers = {'Authorization': f'Bearer {token}'}
    response = test_client.get('/logout', headers=headers)
    assert response.status_code == 200
    assert 'Logged out' in response.get_json()['message']

def test_invalid_user_registration(test_client):
    # Test registration with invalid data
    response = test_client.post('/register', json={
        'username': '',
        'email': 'invalidemail',
        'password': 'short'
    })
    assert response.status_code == 400  # Adjust depending on your error handling
    assert 'Invalid data' in response.get_json()['message']

def test_duplicate_user_registration(test_client):
    # Create a user
    test_client.post('/register', json={
        'username': 'duplicateuser',
        'email': 'duplicateuser@example.com',
        'password': 'password'
    })
    # Attempt to create a user with the same username and email
    response = test_client.post('/register', json={
        'username': 'duplicateuser',
        'email': 'duplicateuser@example.com',
        'password': 'password'
    })
    assert response.status_code == 400  # Adjust depending on your error handling
    assert 'User already exists' in response.get_json()['message']

def test_login_with_invalid_credentials(test_client):
    # Test logging in with invalid credentials
    response = test_client.post('/login', json={
        'username': 'nonexistent',
        'password': 'nope'
    })
    assert response.status_code == 401  # Adjust depending on your error handling
    assert 'Invalid username or password' in response.get_json()['message']
