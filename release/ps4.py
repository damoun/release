# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

from .game import PS4Game


GAME_ZONES = ['JP', 'EU', 'NA']
WIKIPEDIA_PAGES = [
    'https://en.wikipedia.org/wiki/List_of_PlayStation_4_games',
    'https://en.wikipedia.org/wiki/List_of_PlayStation_4_games_(M–Z)'
    'https://en.wikipedia.org/wiki/List_of_PlayStation_4_free-to-play_games'
]


class PS4():
    def __init__(self):
        self.games = []
        for url in WIKIPEDIA_PAGES:
            self.games += self.fetch_games(url)

    def fetch_games(self, url):
        games = []
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        game_rows = iter(soup.find('table', id='softwarelist').find_all('tr'))
        next(game_rows)
        next(game_rows)
        for game_row in game_rows:
            games.append(PS4Game(game_row, GAME_ZONES))
        return games
