import requests
from bs4 import BeautifulSoup


class Song_Scrapper:
    def __init__(self, date):
        self.link = requests.get(f'https://www.billboard.com/charts/hot-100/{date}')
        self.scrape()

    def scrape(self):
        web_data = self.link.text

        soup = BeautifulSoup(web_data, "html.parser")

        songs = soup.select(selector="li h3")

        song_titles = [song.getText().strip("\n") for song in songs[:100]]
        print(song_titles)
