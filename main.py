from spotify_request import Spotify_Request
from date import Date_Check
from songs_list import Song_Scrapper

date = Date_Check()
# Scrapping Part
song_scrapper = Song_Scrapper(date.date)
songlist = song_scrapper.song_list
year = date.date.split('-')[0]

# Spotify Search
sp = Spotify_Request()
# To get all the tracks and remove 'none' tracks
track_uri = [sp.search(song=i, year=year) for i in songlist if not sp.search(song=i, year=year) is None]
print(track_uri)
