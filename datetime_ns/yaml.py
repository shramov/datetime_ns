#!/usr/bin/env python3
# vim: sts=4 sw=4 et

from . import date, datetime, timedelta

import re
import yaml

"""
Code adopted from yaml.constructor.SafeConstructor
"""

timestamp_regexp = re.compile(
        r'''^(?P<year>[0-9][0-9][0-9][0-9])
            -(?P<month>[0-9][0-9]?)
            -(?P<day>[0-9][0-9]?)
            (?:(?:[Tt]|[ \t]+)
            (?P<hour>[0-9][0-9]?)
            :(?P<minute>[0-9][0-9])
            :(?P<second>[0-9][0-9])
            (?:\.(?P<fraction>[0-9]*))?
            (?:[ \t]*(?P<tz>Z|(?P<tz_sign>[-+])(?P<tz_hour>[0-9][0-9]?)
            (?::(?P<tz_minute>[0-9][0-9]))?))?)?$''', re.X)

def construct_yaml_timestamp(self, node):
    value = self.construct_scalar(node)
    match = self.timestamp_regexp.match(node.value)
    values = match.groupdict()
    year = int(values['year'])
    month = int(values['month'])
    day = int(values['day'])
    if not values['hour']:
        return date(year, month, day)
    hour = int(values['hour'])
    minute = int(values['minute'])
    second = int(values['second'])
    fraction = 0
    tzinfo = None
    if values['fraction']:
        fraction = values['fraction'][:9]
        while len(fraction) < 9:
            fraction += '0'
        fraction = int(fraction)
    if values['tz_sign']:
        tz_hour = int(values['tz_hour'])
        tz_minute = int(values['tz_minute'] or 0)
        delta = timedelta(hours=tz_hour, minutes=tz_minute)
        if values['tz_sign'] == '-':
            delta = -delta
        tzinfo = datetime.timezone(delta)
    elif values['tz']:
        tzinfo = datetime.timezone.utc
    return datetime(year, month, day, hour, minute, second, nanosecond=fraction,
                             tzinfo=tzinfo)

def yaml_patch():
    yaml.constructor.SafeConstructor.add_constructor('tag:yaml.org,2002:timestamp', construct_yaml_timestamp)
