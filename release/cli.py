# -*- coding: utf-8 -*-

"""Console script for python_template."""
import os
import sys

import click

from .utils import to_kebab_case
from .calendar import ReleaseCalendar
from .platform import NintendoSwitch, Playstation4, XboxOne


def create_calendars(platform, path):
    console = platform()
    calendars = list(map(ReleaseCalendar, platform.GAME_ZONES))
    for calendar in calendars:
        calendar.populate(console.games)
    for calendar in calendars:
        calendar.write(path)


@click.group()
@click.option('--output', default=".", help='Output to write the files')
@click.pass_context
def cli(ctx, output):
    ctx.ensure_object(dict)
    ctx.obj['output'] = output


@cli.command()
@click.pass_context
def switch(ctx):
    create_calendars(NintendoSwitch, ctx.obj['output'])


@cli.command()
@click.pass_context
def ps4(ctx):
    create_calendars(Playstation4, ctx.obj['output'])


@cli.command()
@click.pass_context
def xboxone(ctx):
    create_calendars(XboxOne, ctx.obj['output'])


if __name__ == "__main__":
    cli()
