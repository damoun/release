# -*- coding: utf-8 -*-

from requests import Session
from bs4 import BeautifulSoup

from .game import Game, NSwitchGame, PS4Game, XOneGame


WIKIPEDIA_BASE_URL = 'https://en.wikipedia.org/wiki/'


class Platform():
    GAME_TYPE = Game
    GAME_ZONES = ['JP', 'NA', 'PAL']
    WIKIPEDIA_PAGES = []

    def __init__(self):
        self.games = []
        self.session = Session()
        for path in self.WIKIPEDIA_PAGES:
            self.games += self.fetch_games(WIKIPEDIA_BASE_URL + path)

    def fetch_games(self, url):
        games = []
        game_rows = self.get_game_rows(url)
        for game_row in game_rows:
            games.append(self.GAME_TYPE(game_row, self.GAME_ZONES))
        return games

    def get_zones(self):
        return self.GAME_ZONES

    def get_game_rows(self, url, ids=None):
        game_rows = []
        if ids is None:
            ids = ['softwarelist', 'f2plist', 'table1']
        html = self.session.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        for html_id in ids:
            table = soup.find('table', id=html_id)
            if table:
                game_rows += table.find_all('tr')[2:]
        return game_rows


class NintendoSwitch(Platform):
    GAME_TYPE = NSwitchGame
    WIKIPEDIA_PAGES = [
        'List of Nintendo Switch games (0–9 and A)',
        'List of Nintendo Switch games (B)',
        'List of Nintendo Switch games (C–G)',
        'List of Nintendo Switch games (H–P)',
        'List of Nintendo Switch games (Q–Z)'
    ]

    def get_game_rows(self, url, ids=None):
        if ids is None:
            ids = ['softwarelist']
        return super(NintendoSwitch, self).get_game_rows(url, ids)


class Playstation4(Platform):
    GAME_TYPE = PS4Game
    WIKIPEDIA_PAGES = [
        'List_of_PlayStation_4_games',
        'List_of_PlayStation_4_games_(M–Z)',
        'List_of_PlayStation_4_free-to-play_games'
    ]

    def get_game_rows(self, url, ids=None):
        if ids is None:
            ids = ['softwarelist', 'f2plist']
        return super(Playstation4, self).get_game_rows(url, ids)


class XboxOne(Platform):
    GAME_TYPE = XOneGame
    WIKIPEDIA_PAGES = [
        'List_of_Xbox_One_games_(A–L)',
        'List_of_Xbox_One_games_(M–Z)'
    ]
