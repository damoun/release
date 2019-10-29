# -*- coding: utf-8 -*-

import re
from datetime import datetime


def to_kebab_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def parse_date(date_string, format='%B %d, %Y'):
    try:
        return datetime.strptime(date_string, format)
    except ValueError:
        return None
