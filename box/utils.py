#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string
import calendar

from django.utils import timezone as dt


def current_user(request):
    steamer = None
    user = request.user
    if user:
        steamer = user
    return steamer


def aware_datetime_to_timestamp(datetime_val):
    if datetime_val:
        return calendar.timegm(datetime_val.timetuple())
    else:
        return 0
