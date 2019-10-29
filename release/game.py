# -*- coding: utf-8 -*-

from .utils import parse_date


class Game():
    def __init__(self, row, zones):
        self.row = row
        self.release_date = {}
        self.parse_title()
        self.parse_release_date(zones)

    def parse_title(self):
        pass

    def parse_release_date(self, zones):
        pass


class NSwitchGame(Game):
    def parse_title(self):
        self.title = self.row.find('th').get_text().strip()

    def parse_release_date(self, zones):
        dates = iter(self.row.find_all('td')[3:])
        for zone in zones:
            self.release_date[zone] = parse_date(
                next(dates).get_text().strip(), fmt='%B %d, %Y'
            )


class PS4Game(Game):
    def parse_title(self):
        self.title = self.row.find('td').get_text().strip()

    def parse_release_date(self, zones):
        dates = iter(self.row.find_all('td')[4:])
        for zone in zones:
            self.release_date[zone] = parse_date(
                next(dates).get_text().strip(), fmt='%b %d, %Y'
            )


class XOneGame(Game):
    def parse_title(self):
        self.title = self.row.find('td').get_text().strip()

    def parse_release_date(self, zones):
        dates = iter(self.row.find_all('td')[4:])
        for zone in zones:
            self.release_date[zone] = parse_date(
                next(dates).get_text().strip(), fmt='%b %d, %Y'
            )
