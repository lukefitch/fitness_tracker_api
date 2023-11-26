# Fitness Tracker API

This is a backend API for a fitness tracking application. The application is built with Flask and uses PostgreSQL for the database. The application is containerized using Docker.

## Installation

1. Clone this repository: [`git clone https://github.com/yourusername/fitness_tracker_api.git`](https://github.com/lukefitch/fitness_tracker_api.git)
2. Navigate to the project directory: `cd fitness_tracker_api`
3. Install dependencies with `pip install -r requirements.txt`.

## Running the Application

1. Run the application with `flask run`.
2. The application will be accessible at `http://localhost:5000`.

## API Endpoints

### POST /users

- Creates a new user.
- Request body: `{ "username": "your_username", "email": "your_email" }`
- Response: `{ "message": "User created" }`

## Database Models

The application uses the following database models:

### User

- `id`: Integer, primary key
- `username`: String, unique, not nullable
- `email`: String, unique, not nullable

### Activity

- `id`: Integer, primary key
- `user_id`: Integer, foreign key to User.id, not nullable
- `type`: String, not nullable
- `duration`: Integer, not nullable
- `intensity`: String, not nullable
- `calories_burned`: Integer, not nullable

### DietLog

- `id`: Integer, primary key
- `user_id`: Integer, foreign key to User.id, not nullable
- `food_item`: String, not nullable
- `calories`: Integer, not nullable
- `serving_size`: String, not nullable

### WorkoutPlan

- `id`: Integer, primary key
- `user_id`: Integer, foreign key to User.id, not nullable
- `plan_details`: Text, not nullable

## Tests

Tests for the application are located in the `tests` directory. To run the tests, use the command `pytest`.

## Docker

To build and run the application using Docker, use the following commands:

1. Build the Docker image: `docker build -t fitness_tracker_api .`
2. Run the Docker container: `docker run -p 5000:5000 fitness_tracker_api`

## Contributing

Contributions are welcome. Please make a pull request.

## License

This project is licensed under the terms of the MIT license.
