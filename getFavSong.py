import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pymongo import MongoClient
import datetime

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')
mongodb_uri = os.getenv('MONGODB_URI')

scope = 'user-top-read'
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        client_id=client_id,
        client_secret=client_secret, 
        redirect_uri=redirect_uri
    )
)

# Connect to MongoDB
client = MongoClient(mongodb_uri)
db = client['favSongswhosfritz']
collection = db['favSongswhosfritz']
time_ranges = ['short_term', 'medium_term', 'long_term']

def returnMyFavSong():
    new = 0
    old = 0    
    for time_range in time_ranges:
        
        results = sp.current_user_top_tracks(
            time_range=time_range,
            limit=1,
            offset=0
        )
    
        if 'items' in results and len(results['items']) > 0:
            song = results['items'][0]
            song_name = song['name']
            song_id = song['id']
            # Convert the date string into a timestamp in format YYYY-MM-DD HH:MM:SS
            song_last_updated = datetime.datetime.now()
            last_checked = datetime.datetime.now()

            # Check if the song already exists in the database
            existing_song = collection.find_one({'spotify_id': song_id, 'time_range': time_range})
            if existing_song is None:
                # Save the song to MongoDB
                song_document = {
                    'spotify_id': song_id,
                    'track_name': song_name,
                    'last_updated': song_last_updated,
                    'last_checked': last_checked,
                    'time_range': time_range
                }
                collection.insert_one(song_document)
                new += 1
            else:
                # Update the last_checked field
                old += 1
                collection.update_one({'spotify_id': song_id}, {'$set': {'last_checked': last_checked}})                
        else:
            print('No songs found for time range: ' + time_range)
    print('New: ' + str(new) + ' Old: ' + str(old) + ' ' + str(last_checked))

# Call the function to get and save the favorite song
returnMyFavSong()

# Close the MongoDB connection
client.close()
