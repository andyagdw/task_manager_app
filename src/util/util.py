'''This module defines a DateUtils class'''

import datetime


class DateUtils():
    '''
    A class used to store date utility methods. It contains three
    methods:
    
    1) ymd_to_datetime_date - Takes in a string in this format
    'YYYY-MM-DD' and converts it into datetime.date
    2) dmy_to_datetime_date - Takes in a string in this format
    'DD-MM-YYYY' and converts it into datetime.date
    3) full_date - Returns the current date as datetime.date
    '''
    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def full_date() -> datetime.date:
        '''
        Returns the current date as <class 'datetime.date'> in this format:
        YYYY-MM-DD
        '''
        todays_date = datetime.date.today()
        return todays_date
