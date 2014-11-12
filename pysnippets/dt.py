# -*- coding: utf-8 -*-
import datetime
import time


def date_to_stamp(date):
    if not date:
        return date
    return time.mktime(date.timetuple())


def date_from_stamp(timestamp):
    if not timestamp:
        return timestamp
    return datetime.date.fromtimestamp(timestamp)


def datetime_from_stamp(timestamp):
    if not timestamp:
        return timestamp
    return datetime.datetime.fromtimestamp(timestamp)

