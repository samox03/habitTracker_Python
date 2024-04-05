
"""
This module takes care of the analysis processes.
Setup of all required actions and validations for a checkoff-event.
"""


from functionality.db import connect_db, fetch_habit_frequency, get_all_streak_archives, get_all_streak_counts, get_period_count, get_streak_archive, get_streak_count, increase_streak_count
import sqlite3
from datetime import date, datetime, timedelta

from functionality.utility import fetch_all_habits_to_select_one


################################################################
# CHECKOFF PROCESSING
################################################################
# Required: 
    # db: habit_analysisdata
    # name
    # frequency
    # start_date
    # period_count
    # streak_count
    # streak_archive

def checkoff_event_handler(name):
        """
        gets triggered once the user tries to checkoff a habit
        - first habit name needs to be choosen from all displayed habits
        - date_now() needs to be compared with the period_counter of the habit: Does the date lays inside an new, unchecked period?
        - if true: add checkoff_date to period_counter list 

            -> also calculate new next_deadline date

        - if true: check with the period_success_checker the period_count list: 
                -> given the according frequency, is a new streak achieved?
                    -> if yes: streak_count +=1 (-> increment_streak())
                    -> else: continue
        """
        # display all habit names from db to choose from
        habit_name = fetch_all_habits_to_select_one()
        
        # checks if checkoff_date lays in new unchecked period:
        period_checker(habit_name):
            # period_count.append(date.now()) && calculate new next_deadline

        if period_checker() == true :
            streak_success_checker(name, period_count)


# TODO:    def period_checker(db, name, new_checkoff_date, period_count()):

def period_checker(habit_name):
        """
        compares the checkoff_date with the period_count. Does the checkoff_date lays in a new period?
        If yes it adds the checkoff date in the period_count attribute. 
        If not, it informs the user.

        :param db: connected sqlite database
        :param new_date: takes the date of checkoff_date() function
        :return: if date lays inside an already checked period -> returns false
        :return: if date lays not inside an already checked period -> returns true and adds the date to the period_count.
        """

        current_date = datetime.now()

        # Get frequency of the choosen habit:
        frequency = fetch_habit_frequency(habit_name)

        # Get period_count of habit
        period_count = get_period_count(habit_name)

        # check if checkoff_date lays in unchecked habit_period
        if frequency == "weekly":
            # Calculate the start of the current week
            start_of_week = current_date - timedelta(days=current_date.weekday())
    
            # Check if there was already a checkoff date in the current period
            for date_str in period_count:
                date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
                if start_of_week <= date <= current_date:
                    print("Oops! This habit already got checked off for the current period.")
                return False
    
            # If no checkoff for the current period exists, add the new date to the period_count list
            period_count.append(current_date.strftime('%Y-%m-%d %H:%M:%S.%f'))
            print("Cool! - Another period success for this habit is registered!")
            return True
            #TODO: If this is true the streak_success_checker needs to be called.


        elif frequency == "daily":
            time_str = current_date.strftime('%Y-%m-%d')
            # Check if there was already a checkoff for that day
            for date_str in period_count:
                date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
                if date.date() == current_date.date():
                    print("Oops! This habit already got checked off for the current period.")
                return False

            # If no checkoff exists, add the new date to the period_count list
            period_count.append(current_date.strftime('%Y-%m-%d %H:%M:%S.%f'))
            print("Cool! - Another period success for this habit is registered!")
            return True
            #TODO: If this is true the streak_success_checker needs to be called.



########################################################################


def streak_success_checker(db, name, period_count, streak_count):

    """
    #former name: streak_control
    Checks if the user reached a 2 Weeks streak by checking the frequency and the period_count. 
    Gets triggert only if period_checker returns true.

    :param db: connected sqlite database
    :param name: name of the habit
    :param period_count: list of recent checkoff dates, is reset to 0 if a streak is archieved.
    :param streak_count: counts every 2 Weeks streak with 1, is reset to 0 if a period is missed.
    """

    frequency = fetch_habit_frequency(name)

    if frequency == 'daily':
        if len(period_count) == 14:
            period_count = 0
            increase_streak_count(name)
            print(f"Cool! You reached a streak of '{len(period_count)}' completed periods for the '{name}' habit!")
            return True

    elif frequency == 'weekly':
        if len(period_count) == 2:
            period_count = 0
            increase_streak_count(name)
            print(f"Cool! You reached a streak of '{len(period_count)}' completed periods for the '{name}' habit!")
            return True

    else:
        return None
    
################################################################
# TRACKING SUCCESS CONTROL:
################################################################
            
def frequency_in_time_checker(name):
        """
        checks if a habit got a checkoff in time of the set period:
            -> startdate + frequency -> next_deadline
            -> if next_deadline = lays in the past
                -> display fail message
                -> add streak_count to streak_archive
                -> reset streak_count
                -> reset period_count
        """

        frequency = fetch_habit_frequency(name)


# TODO:    def increment_streak_count(db, self.name, date):

# TODO:    def add_streak_count(db, self.name, self.frequency)

################################################################
# MAIN ANALYSIS FUNCTIONS:
################################################################



    # Return the longest run streak for a given habit
def longest_streak_given_habit(habit_name):
    """
    Compare streak_count and streak_archive of given number for highest number in the lists.
    """
    current_streak_count = get_streak_count(habit_name)
    current_streak_archive = get_streak_archive(habit_name)
    # calculate highest nr
    highest_streak = max(current_streak_count, current_streak_archive)

    return highest_streak


    # Return the habit with the longest streak:
def longest_streak_all_habits():
    """
    Compare streak_count and streak_archive of all habits for highest number in the lists.
    Returns the highest streak count and the name of that habit.
    """
    all_streak_counts = get_all_streak_counts()
    all_streak_archives = get_all_streak_archives()
    
    # calculate highest nr
    highest_streak_count = max([streak[0] for streak in all_streak_counts + all_streak_archives])

    # access name 
    habit_name = [streak[1] for streak in all_streak_counts + all_streak_archives if streak[0] == highest_streak_count][0]

    return highest_streak_count, habit_name


    # Display the habit with the shortest streak success
    # Alternative: check lowest streak rate in last 2 weeks

    # def shorteststreakhabit():
    # """
    # "With which habit did the user struggle the most in den letzten 2 Wochen?" -> wird definiert als: lowest streak durchschnitt.
    # calculate: 
    # date.today - start_day = x Tage, 
    # len(streak_archive (if 0 take streak_count (if 0 take len(period_count)))
    # -> tage / number_of_streaks -> niedrigste nummer -> struggled the most.
    # Add all streak_count and streak_archive length, attributes for the lowest number.
    # """
    # TODO: add content

################################################################
#TODO: DELETE later:







################################################################