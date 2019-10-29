# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

from .game import NSwitchGame, PS4Game


WIKIPEDIA_BASE_URL = 'https://en.wikipedia.org/wiki/'


class Platform():
    GAME_ZONES = ['JP', 'EU', 'NA']
    WIKIPEDIA_PAGES = []

    def __init__(self):
        self.games = []
        for path in self.WIKIPEDIA_PAGES:
            self.games += self.fetch_games(WIKIPEDIA_BASE_URL + path)

    def fetch_games(self, url):
        pass

    def get_zones(self):
        return self.GAME_ZONES


class NintendoSwitch(Platform):
    GAME_ZONES = ['JP', 'NA', 'PAL']
    WIKIPEDIA_PAGES = [
        'List_of_Nintendo_Switch_games',
        'List_of_Nintendo_Switch_games_(M–Z)'
    ]

    def fetch_games(self, url):
        games = []
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        game_rows = iter(soup.find('table', id='softwarelist').find_all('tr'))
        next(game_rows)
        next(game_rows)
        for game_row in game_rows:
            games.append(NSwitchGame(game_row, self.GAME_ZONES))
        return games


class Playstation4(Platform):
    WIKIPEDIA_PAGES = [
        'List_of_PlayStation_4_games',
        'List_of_PlayStation_4_games_(M–Z)',
        'List_of_PlayStation_4_free-to-play_games'
    ]

    def fetch_games(self, url):
        games = []
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        game_rows = iter(soup.find('table', id='softwarelist').find_all('tr'))
        next(game_rows)
        next(game_rows)
        for game_row in game_rows:
            games.append(PS4Game(game_row, self.GAME_ZONES))
        return games
