import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pymongo import MongoClient
import time

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')
mongodb_uri = os.getenv('MONGODB_URI')

scope = 'user-top-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                               client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri))

# Connect to MongoDB
client = MongoClient(mongodb_uri)
db = client['favSongswhosfritz']
collection = db['favSongswhosfritz']

def returnMyFavSong():
    results = sp.current_user_top_tracks(time_range="short_term", limit=1, offset=0)
    if 'items' in results and len(results['items']) > 0:
        song = results['items'][0]
        song_name = song['name']
        song_id = song['id']
        # Convert the date string into a timestamp in format YYYY-MM-DD HH:MM:SS
        song_last_updated = time.strftime('%Y-%m-%d %H:%M:%S')
        
        # Check if the song already exists in the database
        existing_song = collection.find_one({'spotify_id': song_id})
        if existing_song is None:
            # Save the song to MongoDB
            song_document = {
                'spotify_id': song_id,
                'track_name': song_name,
                'last_updated': song_last_updated,
            }
            collection.insert_one(song_document)

# Call the function to get and save the favorite song
returnMyFavSong()

# Close the MongoDB connection
client.close()
