from datetime import datetime, date
from functionality.get import frequency_change_confirmed, habit_delete_confirmed, habit_frequency, habit_name
from functionality.db import add_habit, connect_db, habit_exists


# TODO: adjust database name end of line 6
class Habit:
    def __init__(self, name: str, description: str, frequency: str, database="main.db"):
        self.name = name
        self.description = description
        self.frequency = frequency
        self.db = connect_db(database)
        # self.start_date = datetime.now().strftime("%m/%d/%Y %H:%M")
        self.start_date = date.today()
        self.period_count = []
        self.streak_count = 0
        self.streak_archive = 0
        


# the following functionality shall be implemented here:
    # create_new_habit
    # edit_habit
    # delete_habit
    # checkoff_a_habit
        # -> the check_off works like this: the users chooses the habit that he wants to check off.
        # the period_counter counts +1. The period counter checks if the sum is 30 (daily habits) and if the sum is 4 (weekly habits).
        # If the check of the period_counter is true, the streak_counter counts +1 and the user gets a success message.
        # Also the period_counter checks if the startday of the streaktime minus the date of the day is 4 (weekly habits) or 30 (daily habits).
        # If the latter calculation is true, but there was noc streak that day, then the user gets a reminding message that the streak was interrupted.


# create_new_habit
    def add_habit(self):
        """
        Create a new habit to the db based on user inputs.
        """
        habit_name()
        habit_frequency()
        if not habit_exists(self.db, self.name):
            add_habit(self.db, self.name, self.description, self.frequency, self.current_time)
            print(f"\nThe habit '{self.name.capitalize()}' has been written to the db as a '{self.frequency.capitalize()}' "
                  f"Habit starting from '{self.current_time}'.\n")
        else:
            print("\nHabit already exists, please edit the habit from the database or define another habit.\n")


# edit_habit
    def change_frequency(self, new_frequency):
        """
        Changes the habit frequency.
        """

        self.frequency = new_frequency
        if frequency_change_confirmed():
            db.update_frequency(self.db, self.name, self.frequency)
            print(f"\nThe frequency of the Habit '{self.name.capitalize()}' got changed to '{self.frequency.capitalize()}'.\n")
        else: return

# delete_habit
    def delete(self):
        """
        Removes the habit from the habit_tracker database.
        """
        if habit_delete_confirmed():
            db.delete_habit(self.db, self.name)
            print(f"\n'{self.name.capitalize()}' got deleted from the database successfully.\n")
        else: return


# TODO: implement the streak management.... -> im counter oder analyze file
# def increment_streak(self):
# def reset_streak(self):
# def update_streak(self):

# checkoff_habit_event
#    def checkoff(self):
        """
        Checks the frequency of the habit .......
        """