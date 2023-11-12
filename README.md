# 🎵 Spotify API - whosFritz

This project utilizes the Spotify API to display the user's favorite song based on the last 4 weeks. The backend is built with Flask, and the data is stored in MongoDB.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The purpose of this project is to provide a simple backend service that interacts with the Spotify API to retrieve the user's favorite song from the last 4 weeks. The Flask application serves as an API endpoint that can be integrated into a website to display the user's favorite song dynamically.

## Features

- Retrieves the user's favorite song from the last 4 weeks using the Spotify API.
- Stores the song data in a MongoDB database for future reference.
- Provides a Flask API endpoint for easy integration into web applications.
- Demonstrates how to use environment variables for secure configuration.

## Getting Started

### Prerequisites

Before running the application, you need to have the following installed:

- Python (version 3.6 or higher) 🐍
- Pip (Python package installer) 📦
- MongoDB (Make sure the MongoDB server is running) 🚀

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/whosFritz/spotify-api-whosfritz.git
   ```

2. Navigate to the project directory:

   ```bash
   cd spotify-api-whosfritz
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1.  Set up your Spotify API credentials and MongoDB URI by creating a .env file in the project root:

    ```bash
    SPOTIPY_CLIENT_ID=your_client_id
    SPOTIPY_CLIENT_SECRET=your_client_secret
    SPOTIPY_REDIRECT_URI=your_redirect_uri
    MONGODB_URI=your_mongodb_uri
    ENDPOINT_PATH=/your/api/endpoint
    ```

2.  Run the Flask application:

    ```bash
    python app.py
    ```

3.  Access the API endpoint in your web browser or integrate it into your website.

    The API endpoint is accessible at:

    ```bash
    curl http://localhost:8088/your/api/endpoint
    ```

    This endpoint returns JSON data containing the user's favorite song information.

### Contributing

Feel free to contribute to this project. You can submit bug reports, feature requests, or even open a pull request. 🤝

### License

This project is licensed under the [MIT License](LICENSE) 📄
