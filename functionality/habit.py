from datetime import datetime, date
from functionality.utility import frequency_change_confirmation, get_startdate, habit_delete_confirmation, habit_frequency, habit_name
from functionality.db import add_habit, connect_db, delete_habit, fetch_all_habits, habit_exists, update_frequency_alltables


# TODO: adjust database name end of line 6
class Habit:
    def __init__(self, name: str, description: str, frequency: str, start_date: str, database="main.db"):
        # def __init__(self, name: str, description: str, frequency: str, start_date: date, database="main.db"):
        self.name = name
        self.description = description
        self.frequency = frequency
        self.db = connect_db(database)
        self.start_date = start_date
        self.period_count = []
        self.streak_count = 0
        self.streak_archive = []
        

# the following functionality shall be implemented here:
    # create_new_habit
    # edit_habit
    # delete_habit
    # checkoff_a_habit
        # -> the check_off works like this: the users chooses the habit that he wants to check off.
        # the period_count counts +1. The period counter checks if the sum is 30 (daily habits) and if the sum is 4 (weekly habits).
        # If the check of the period_count is true, the streak_count counts +1 and the user gets a success message.
        # Also the period_count checks if the startday of the streaktime minus the date of the day is 4 (weekly habits) or 30 (daily habits).
        # If the latter calculation is true, but there was noc streak that day, then the user gets a reminding message that the streak was interrupted.

# create_new_habit
    def add(self):
        """
        Create a new habit to the db based on user inputs.
        """
        # habit_name()
        # habit_frequency()
        if not habit_exists(self.db, self.name):
            add_habit(self.db, self.name, self.description, self.frequency)
            print(f"\nThe habit '{self.name.capitalize()}' has been written to the db as a '{self.frequency.capitalize()}'\n")
        else:
            print("\nHabit already exists, please edit the habit from the database or define another habit.\n")


# edit_habit
    def change_frequency(self, new_frequency):
        """
        Changes the habit frequency.
        """

        self.frequency = new_frequency
        if frequency_change_confirmation():
            update_frequency_alltables(self.db, self.name, self.frequency)
            print(f"\nThe frequency of the Habit '{self.name.capitalize()}' got changed to '{self.frequency.capitalize()}'.\n")
        else: return

#TODO: update_description -> not implemented yet
    # def change_description(self, new_description):
    #     """
    #     Changes the habit frequency.
    #     """

    #     self.description = new_description
    #     if frequency_change_confirmation():
    #         update_description(self.db, self.name, self.description)
    #         print(f"\nThe description of the Habit '{self.name.capitalize()}' got changed to '{self.description}'.\n")
    #     else: return

# delete_habit
    def delete(self):
        """
        Removes the habit from the habit_tracker database.
        """
        if habit_delete_confirmation():
            delete_habit(self.db, self.name)
            print(f"\n'{self.name.capitalize()}' got deleted from the database successfully.\n")
        else: return


################################################################
# Check-off a habit (hier in der Klasse definieren???)
        #TODO: Decide where to implement the checkoff-event -> functional
################################################################

    def checkoff_event_handler(self):
        """
        Gets triggered when the user tries to check off a habit.
        - first habit name needs to be choosen from all displayed habits
        - date_now() needs to be compared with the period_counter: Does the date lays inside an new, unchecked period?
        - if true: add checkoff_date to period_counter list (-> increment_streak())

            -> also calculate new next_deadline date
        - if true: check with the period_success_checker the period_counter list: 
                -> given the according frequency, is a new streak achieved?
                    -> if yes: streak_count +=1
                    -> else: continue
        """


    def check_period_missed():
        """
        Is called when the user starts the programm.
        Usecase: Check if the user keeps track on checking off habits in the choosen time.
        
        - iterates through the entire database and checks for each habit:
            - what is the period in which the habit should be checked off according to the start date and the frequency.
            - Does the last entry in the period_counter lays in the current or last period?
            - Is the last period unchecked but gone?

            - if last period remained unchecked:
                -> display fail message on CLI
                -> append streak_count to streak_archive
                -> reset streak_count
                -> reset period_count

        """

        current_date = datetime.now()
    
        # Fetch all habits from the database   
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



       


