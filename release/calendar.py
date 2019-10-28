# -*- coding: utf-8 -*-

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

    def write(self, path):
        file = open("%s/%s.ics" % (path, self.zone), 'wb')
        file.write(self.cal.to_ical())
        file.close()
