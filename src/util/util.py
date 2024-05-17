'''This module defines utiliy functions'''

import datetime


def ymd_to_datetime_date(date_string: str) -> datetime.date:
    '''
    Takes in a string in YYYY-MM-DD format:

    Used when retrieving a date from database (SQLite
    stores date in this format). The input is then converted into
    <class 'datetime.date'> and the date is returned as YYYY-MM-DD
    '''
    new_date = (datetime.datetime
                .strptime(date_string, "%Y-%m-%d").date())
    return new_date


def dmy_to_datetime_date(date_string: str) -> datetime.date:
    '''
    Takes in a string in DD-MM-YYYY format:

    Used when retrieving input from the user when creating a task.
    The input is then converted into <class 'datetime.date'> and the
    date is returned as YYYY-MM-DD
    '''
    new_date = (datetime.datetime
                .strptime(date_string, "%d-%m-%Y").date())
    return new_date


def full_date() -> datetime.date:
    '''
    Returns the current date as <class 'datetime.date'> in this format:
    YYYY-MM-DD
    '''
    todays_date = datetime.date.today()
    return todays_date
