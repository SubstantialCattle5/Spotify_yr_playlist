from bs4 import BeautifulSoup
from date import Date_Check
import requests

text = requests.get(
    'https://www.billboard.com/charts/hot-100/2016-08-20/')

soup = BeautifulSoup(text.text, 'html.parser')
songs = soup.select(selector="li h3")

song_titles = [song.getText().strip("\n") for song in songs[:100]]
print(song_titles)