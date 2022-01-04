import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv("E:\PROJECTS\python\spotify_year_playlist\.env.txt")
CLIENT_ID = os.getenv('client_id')
CLIENT_SECRET = os.getenv('client_secret')
REDIRECT_URI = 'https://example.com/'


class Spotify_Request:
    def __init__(self):
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope="playlist-modify-public",
                redirect_uri=REDIRECT_URI,
                client_id=CLIENT_ID,
                client_secret=CLIENT_SECRET,
                show_dialog=True,
                cache_path="E:\PROJECTS\python\spotify_year_playlist\\token.txt"
            )
        )

        self.user_id = self.sp.current_user()["id"]
        self.search()

    def search(self):
        result = self.sp.search(q=f'track:The Shell Shack', type='track')
        print(result)
