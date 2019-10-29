# -*- coding: utf-8 -*-

import re
from datetime import datetime


def to_kebab_case(name):
    sub_string = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1-\2', sub_string).lower()


def parse_date(date_string, fmt='%B %d, %Y'):
    try:
        return datetime.strptime(date_string, fmt)
    except ValueError:
        return None
