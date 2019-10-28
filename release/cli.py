# -*- coding: utf-8 -*-

"""Console script for python_template."""
import sys

import click

from .calendar import ReleaseCalendar
from .nswitch import NintendoSwitch, GAME_ZONES


@click.command()
def main():
    """Console script for python_template."""
    nswitch = NintendoSwitch()
    calendars = list(map(ReleaseCalendar, GAME_ZONES))
    for game in nswitch.games:
        for calendar in calendars:
            calendar.add_release(game)
    for calendar in calendars:
        calendar.write('nintendo-switch')
    return 0


if __name__ == "__main__":
    sys.exit(main())
