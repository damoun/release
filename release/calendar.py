# -*- coding: utf-8 -*-

import os

from icalendar import Calendar, Event


class ReleaseCalendar():
    def __init__(self, zone):
        self.zone = zone
        self.cal = Calendar()

    def add_release(self, game):
        if game.release_date[self.zone]:
            event = Event()
            event.add('summary', game.title)
            event.add('dtstart', game.release_date[self.zone])
            self.cal.add_component(event)

    def populate(self, games):
        for game in games:
            self.add_release(game)

    def write(self, path):
        filename = os.path.join(path, self.zone + '.ics')
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        file = open(filename, 'wb')
        file.write(self.cal.to_ical())
        file.close()
