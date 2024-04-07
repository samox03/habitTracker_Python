
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
    

#######################################

#######################################
#######################################
#######################################
#######################################
#######################################


# TODO: An richtige Codestelle einfuegen, hier nur test purpose
    
    def check_period_missed():
        """
        Is called when the user starts the programm.
        Usecase: Check if the user keeps track on checking off habits in the choosen time.
        
        - iterates through the entire database and checks for each habit:
            - what is the period in which the habit should be checked off according to the start date and the frequency.
            - Does the last entry in the period_counter lays in the current or last period?
            - Is the last period unchecked but gone?

        If a habit period has expired, a reminding message is displayed on the CLI.

        """

        current_date = datetime.now()
    
        # Fetch all habits from the database   
        # TODO: implement fetch_all_habits 
        habits = fetch_all_habits()  
    

        for habit in habits:
        # Check current habit frequency and get period count
            frequency = habit.get("frequency")
            period_count = habit.get("period_count")

            if frequency == "weekly":
            # Calculate the start of the current period based on start_date from the habit
                start_date = datetime.strptime(habit.get("start_date"), '%Y-%m-%d %H:%M:%S.%f')
                period_length = 7  # For weekly frequency
                weeks_passed = (current_date - start_date).days // period_length

            # Check if the current date is in a new period
            if len(period_count) == 0 or period_count[-1] != current_date.strftime('%Y-%m-%d %H:%M:%S.%f'):
                if (current_date - start_date).days >= (weeks_passed * period_length):
                    period_count.append(current_date.strftime('%Y-%m-%d %H:%M:%S.%f'))
                else:
                    print(f"WARNING: You missed checking off {habit.get('name')}. Its Period expired without any checkoff :/ .")
                    

            elif frequency == "daily":
                # Check if the current date is in a new period (daily frequency)
                if len(period_count) == 0 or period_count[-1] != current_date.strftime('%Y-%m-%d %H:%M:%S.%f'):
                    if current_date.date() == datetime.strptime(habit.get("start_date"), '%Y-%m-%d %H:%M:%S.%f').date():
                        period_count.append(current_date.strftime('%Y-%m-%d %H:%M:%S.%f'))
                    else:
                        print(f"WARNING: You missed checking off {habit.get('name')}. Its Period expired without any checkoff :/ .")

