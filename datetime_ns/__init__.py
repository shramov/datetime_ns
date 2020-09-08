#!/usr/bin/env python3
# vim: sts=4 sw=4 et

import sys
from . import datetime as module
from .datetime import *

def datetime_patch():
    sys.modules['datetime'] = module
    for n in ("date", "datetime", "time", "timedelta", "timezone", "tzinfo"):
        c = getattr(module, n)
        if hasattr(c, '__module__'):
            c.__module__ = 'datetime'

