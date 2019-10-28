# -*- coding: utf-8 -*-

from datetime import datetime


def parse_date(date_string):
    try:
        return datetime.strptime(date_string, '%B %d, %Y')
    except ValueError:
        return None
