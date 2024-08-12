# SocialPulse

SocialPulse is a robust social media backend built with FastAPI, utilizing Docker and PostgreSQL for seamless deployment and database management. It provides essential features for user authentication, JWT-based security, and efficient post management. The project also includes automated testing with pytest, ensuring code reliability and quality. SocialPulse is a solid foundation for building social media applications, with easy setup and comprehensive features.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Authentication:** Secure user login with password hashing.
- **JWT Authentication:** Provides JWT token generation with expiration for secure API access.
- **Post Management:** Create, fetch single posts, update posts, delete posts, like posts, and fetch all posts.
- **Docker Support:** Easily set up and run the project using Docker Compose.
- **Environment Configuration:** Example environment files (`.env.example` and `.env.postgres.example`) to help you get started quickly.

## Installation

### Prerequisites

- Docker
- Docker Compose

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/resist15/SocialPulse.git
    cd SocialPulse
    ```

2. Copy the example environment variable files and configure them as needed:

    ```bash
    cp .env.example .env
    cp .env.postgres.example .env.postgres
    ```

3. Build and run the containers using Docker Compose:

    ```bash
    docker-compose up --build
    ```

    This will start the FastAPI application along with any required services like the database.

4. The application will be running at `http://127.0.0.1:8000`.

## Usage

### Access the API

1. **Interactive API Documentation:**

   - Open your browser and navigate to `http://127.0.0.1:8000/docs` for the Swagger UI.
   - Or go to `http://127.0.0.1:8000/redoc` for ReDoc.

2. **Test the API Endpoints:**

   You can use the interactive documentation to test the endpoints directly from your browser.

## API Endpoints

- **Authentication:**
  - `POST /auth/`: Authenticate a user and receive a JWT token.
- **User Management:**
  - `POST /users/`: Create a new user.
  - `GET /users/{id}/`: Fetch the current user's details.
- **Post Management:**
  - `POST /posts/`: Create a new post.
  - `GET /posts/{id}`: Fetch a single post by ID.
  - `GET /posts/`: Fetch all posts.
  - `PUT /posts/{id}`: Update post.
  - `DEL /posts/{id}`: Delete post.
  - `POST /like/`: Like a post.

### Example Request: User Login

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/auth/' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "user1",
  "password": "password123"
}'
```
### Example Response: JWT Token

```
{
  "access_token": "your.jwt.token",
  "token_type": "bearer"
}
```
## Configuration

The application uses environment variables for configuration. Example environment variable files have been provided:

- **`.env.example`**: General environment variables for the application.
- **`.env.postgres.example`**: Environment variables specific to PostgreSQL configuration.

To use them:

1. Copy the example files to `.env` and `.env.postgres`.
2. Edit the files to include your specific configuration details, such as database credentials, JWT secret keys, etc.

Docker Compose will automatically load these environment variables.

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

