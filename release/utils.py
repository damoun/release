# -*- coding: utf-8 -*-

from datetime import datetime


def parse_date(date_string, format='%B %d, %Y'):
    try:
        return datetime.strptime(date_string, format)
    except ValueError:
        return None
