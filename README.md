# 🎵 Spotify API - whosFritz

This project utilizes the Spotify API with the [spotipy](https://github.com/spotipy-dev/spotipy) library to display my favorite song on my website based on the last 4 weeks, 6 months and over several years. The backend is built with python, and the data is stored in MongoDB. MongoDB was chosen for its document-based data architecture.

![how it works](how-it-works-now.png)

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

The purpose of this project is to provide a simple backend service that interacts with the Spotify API to retrieve the user's favorite song from the last 4 weeks.

**Note:**
For security reasons, this project does not directly connect to the Spotify API from the client side. Instead, a dockerized script on the backend fetches data from the Spotify API by schedule, ensuring that sensitive information like API credentials are not exposed to the public. Additionally, to mitigate potential issues with the Spotify API rate limits or downtimes, the retrieved data is saved in a MongoDB database, providing a more reliable experience for users. The data in the MongoDB is then used on my own portfolio website www.whosfritz.de

- Retrieves the user's favorite song from the past weeks, months, years using the Spotify API.
- Stores the song data in a MongoDB database for future reference.

## Getting Started

### Prerequisites

Before running the application, you need to have the following installed:

- Python3 🐍
- Pip (Python package installer) 📦
- MongoDB (Make sure the MongoDB server is running) 🚀
- Try it first on your local machine.

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

1. Set up your Spotify Dev Accout [here](https://developer.spotify.com/dashboard)
2. Create an App and define the callback-url
3. Set up your Spotify API credentials and MongoDB URI by creating a .env file in the project root:

   ```bash
   SPOTIPY_CLIENT_ID=your_client_id
   SPOTIPY_CLIENT_SECRET=your_client_secret
   SPOTIPY_REDIRECT_URI=your_redirect_uri
   MONGODB_URI=your_mongodb_uri
   DB_NAME=your_db_name
   COLLECTION_NAME=your_collection_name
   ```

4. Run the script:

   ```bash
   python app.py
   ```
   
### Contributing

Feel free to contribute to this project. You can submit bug reports, feature requests, or even open a pull request. 🤝

### License

This project is licensed under the [MIT License](LICENSE) 📄
