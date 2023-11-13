from flask import Flask, jsonify
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
mongodb_uri = os.getenv('MONGODB_URI')
endpoint_path = os.getenv('ENDPOINT_PATH', '/spotifywhosfritz')  # Default value is '/spotifywhosfritz'

# Define Flask app
app = Flask(__name__)

# Connect to MongoDB
client = MongoClient(mongodb_uri)
db = client['favSongswhosfritz']
collection = db['favSongswhosfritz']

@app.route(endpoint_path, methods=['GET'])
def endpointFavSong():
    # Retrieve the latest song from MongoDB
    song_document = collection.find_one(sort=[('_id', -1)])
    if song_document:
        song_name = song_document['track_name']
        song_id = song_document['spotify_id']
        song_last_updated = song_document['last_updated']
        song_llast_checked = song_document['last_checked']      
        response = jsonify(
            fav_Song_ID=song_id,
            fav_Song_Name=song_name, 
            last_Updated=song_last_updated,
            last_Checked=song_llast_checked
        )
    else:
        response = jsonify(error="No favorite song found.")
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8088)