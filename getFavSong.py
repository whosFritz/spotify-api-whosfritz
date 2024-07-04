import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pymongo import MongoClient
import datetime
import schedule
import time
import logging

# Load environment variables from .env file
load_dotenv()

# Setup logging
log_file_path = '/logs/spotify_fetch.log'
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(message)s')

# Retrieve environment variables
client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')
mongodb_uri = os.getenv('MONGODB_URI')
db_name = os.getenv('DB_NAME')
collection_name = os.getenv('COLLECTION_NAME')

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
db = client[db_name]
collection = db[collection_name]
time_ranges = ['short_term', 'medium_term', 'long_term']

def returnMyFavSong():
    new = 0
    old = 0    
    changes = []
    
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
            song_last_updated = datetime.datetime.now()
            last_checked = datetime.datetime.now()

            existing_song = collection.find_one({'spotify_id': song_id, 'time_range': time_range})
            if existing_song is None:
                song_document = {
                    'spotify_id': song_id,
                    'track_name': song_name,
                    'last_updated': song_last_updated,
                    'last_checked': last_checked,
                    'time_range': time_range
                }
                collection.insert_one(song_document)
                new += 1
                changes.append(f'New song added: {song_name} for time range {time_range}')
            else:
                old += 1
                if existing_song['track_name'] != song_name:
                    changes.append(f'Changed song for time range {time_range}: {existing_song["track_name"]} to {song_name}')
                collection.update_one({'spotify_id': song_id}, {'$set': {'last_checked': last_checked}})
        else:
            print(f'No songs found for time range: {time_range}')
            logging.info('No songs found for time range: %s', time_range)
    
    log_message = f'{last_checked.strftime("%Y-%m-%d %H:%M:%S.%f")} - New: {new} Old: {old}'
    if changes:
        log_message += '\n' + '\n'.join(changes)
    
    print(log_message)
    logging.info(log_message)

# Run the function once when the script starts
returnMyFavSong()

# Schedule the job to run every 6 hours
schedule.every(6).hours.do(returnMyFavSong)

# Execution loop
while True:
    schedule.run_pending()
    time.sleep(1)

# Close the MongoDB connection when the script stops
client.close()
