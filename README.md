# Fitness Tracker API

This is a backend API for a fitness tracking application.

## Installation

1. Clone this repository.
2. Install dependencies with `pip install -r requirements.txt`.
3. Run the application with `flask run`.

## Usage

POST /users
- Creates a new user.
- Request body: `{ "username": "your_username", "email": "your_email" }`
- Response: `{ "message": "User created" }`
