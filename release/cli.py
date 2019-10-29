# -*- coding: utf-8 -*-

"""Console script for python_template."""
import sys

import click

from .utils import to_kebab_case
from .calendar import ReleaseCalendar
from .platform import NintendoSwitch, Playstation4


def create_calendars(platform):
    console = platform()
    calendars = list(map(ReleaseCalendar, platform.GAME_ZONES))
    for calendar in calendars:
        calendar.populate(console.games)
    for calendar in calendars:
        calendar.write(to_kebab_case(platform.__name__))


@click.command()
def main():
    """Console script for python_template."""
    consoles = [NintendoSwitch, Playstation4]
    for console in consoles:
        create_calendars(console)
    return 0


if __name__ == "__main__":
    sys.exit(main())
