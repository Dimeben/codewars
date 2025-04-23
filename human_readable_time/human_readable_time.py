"""
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)
"""

import math


## My solution:
def make_readable(seconds):
    if seconds == 0:
        return "00:00:00"

    readable_hours = "00"
    readable_minutes = "00"
    readable_seconds = ""
    one_hour = 3600
    one_minute = 60

    if seconds <= 59:
        readable_seconds = f"{seconds}"

    elif seconds >= 60 and seconds <= 3599:
        minutes = math.floor(seconds / one_minute)
        readable_minutes = f"{minutes}"
        remaining_seconds = seconds - minutes * one_minute
        readable_seconds = f"{remaining_seconds}"

    else:
        hours = math.floor(seconds / one_hour)
        readable_hours = f"{hours}"
        remaining_seconds = seconds - hours * one_hour
        minutes = math.floor(remaining_seconds / one_minute)
        readable_minutes = f"{minutes}"
        remaining_seconds -= minutes * one_minute
        readable_seconds = f"{remaining_seconds}"

    ## Checks if each unit has 2 digits. If it doesn't, it prepends a 0:

    if len(readable_hours) == 1:
        readable_hours = f"0{readable_hours}"

    if len(readable_minutes) == 1:
        readable_minutes = f"0{readable_minutes}"

    if len(readable_seconds) == 1:
        readable_seconds = f"0{readable_seconds}"

    return f"{readable_hours}:{readable_minutes}:{readable_seconds}"


## Best solution on Codewars:


def make_readable_best(seconds):
    hours, seconds = divmod(seconds, 60**2)
    minutes, seconds = divmod(seconds, 60)
    return "{:02}:{:02}:{:02}".format(hours, minutes, seconds)
