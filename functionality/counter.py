
"""
While the anlysis module takes care of the checkoff functionality, 
the counter class stores the period and streak values and allows to acces them. 
As it is focused more on storing values instead of processing them 
it is composed as a class following the OOP approach.
"""

import functionality.db as db
from datetime import datetime, timedelta


class Counter:
    def __init__(self, name:str, frequency:str, period_count:int, streak_archive:int, streak_count:int, database="main.db"):
        self.name = name 
        self.frequency = frequency
        self.period_count = period_count
        self.streak_archive = streak_archive
        self.streak_count = streak_count
        self.check_off_date
        self.db = db.connect_database(database)

# Counting
    def period_increment(self):
        self.period_count += 1

    def streak_increment(self):
        self.streak_count += 1

    def period_reset(self):
        self.period_count = 0

    def streak_reset(self):
        self.streak_count = 0


# show period_count:
    def __str__(self):
        return f"For the habit {self.name} {self.period_count} of successful periods in a row got tracked."

# show streak_count:
    def __str__(self):
        return f"For the habit {self.name} {self.streak_count} fullfilled streaks in a row got tracked."
        
# show streak_archive:
    def __str__(self):
         return f"For the habit {self.name} the highest nr of streaks in a row was {self.streak_archive}."


#######################################
# Connect to the database/ example:
# TODO: add_counter() und increament_counter() sollten im db file definiert werden und hier importiert
def store(self, db):
    add_counter(db, self.name, self.frequency)

def add_event(self, db, date: str=None):
    increment_counter(db, self.name, date)
#######################################
    

