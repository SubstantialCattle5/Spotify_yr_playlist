import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv("E:\PROJECTS\python\spotify_year_playlist\.env.txt")  # Enter your own local env
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

    def search(self, song, year):
        result = self.sp.search(q=f'track:{song} year:{year}', type='track')
        try:
            uri = result["tracks"]["items"][0]["uri"]
            return uri
        except IndexError:
            print(f'{song} not Found')

    def playlist(self, songlist, year):

            # Creating the playlist
            playlist = self.sp.user_playlist_create(user=self.user_id, name=f'Top Songs of year: {year}', public=True,
                                                    collaborative=False, description='')
            # Adding songs to the playlist
            self.sp.playlist_add_items(playlist_id=playlist['id'], items=songlist, position=None)
            print("Successful")
