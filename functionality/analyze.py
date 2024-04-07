
"""
This module takes care of the analysis processes.
Setup of all required actions and validations for a checkoff-event.
"""


from functionality.db import connect_db, fetch_all_habits, fetch_habit_frequency, get_all_streak_archives, get_all_streak_counts, get_period_count, get_streak_archive, get_streak_count, increase_streak_count
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

def checkoff_event_handler(db, name):
        """
        gets triggered once the user tries to checkoff a habit
            - period_checker checks if the date lays inside an new, unchecked period.
            - if true: 
                    - add checkoff_date to period_counter list 
                    - the streak_success_checker checks the period_count list for a streak and updates the counters.
        """
        
        # checks if checkoff_date lays in new unchecked period of the choosen habit:
        if period_checker(name) == True:
            print("Cool! - Another period success for this habit is registered!")
            streak_success_checker(name)

        else:
            print("This habit already got checked off for the current period!")


            # TODO: DELETE: period_count.append(datetime.now()) && calculate new next_deadline



def period_checker(db, habit_name):
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
                #date formation
                date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
                if start_of_week.date() <= date.date() <= current_date.date(): return False
    
            # If no checkoff for the current period exists, add the new date to the period_count list
            period_count.append(current_date.strftime('%Y-%m-%d %H:%M:%S.%f'))
            return True


        elif frequency == "daily":
            time_str = current_date.strftime('%Y-%m-%d')
            # Check if there was already a checkoff for that day
            for date_str in period_count:
                #date formation
                date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
                if date.date() == current_date.date(): return False
                

            # If no checkoff exists, add the new date to the period_count list
            period_count.append(current_date.strftime('%Y-%m-%d %H:%M:%S.%f'))
            return True



def streak_success_checker(name):

    """
    #former name: streak_control
    Checks if the user reached a 2 Weeks streak by checking the frequency and the period_count. 
    Gets triggert only if period_checker returns true.

    :param db: connected sqlite database
    :param name: name of the habit
    :param period_count: list of recent checkoff dates, is reset to 0 if a streak is archieved.
    :param streak_count: counts every 2 Weeks streak with 1, is reset to 0 if a period is missed.
    """

    period_count = get_period_count(name)

    frequency = fetch_habit_frequency(name)

    if frequency == 'daily':
        if len(period_count) == 14:
            period_count = 0
            increase_streak_count(name)
            print(f"Cool! You reached a streak of '{len(period_count)}' completed periods for the '{name}' habit!")
            return True
        else: False

    elif frequency == 'weekly':
        if len(period_count) == 2:
            period_count = 0
            increase_streak_count(name)
            print(f"Cool! You reached a streak of '{len(period_count)}' completed periods for the '{name}' habit!")
            return True
        else: False

    else:
        return None
    
################################################################
# TRACKING SUCCESS CONTROL:
################################################################
            
# def frequency_in_time_checker(self):
#         """
#         checks if a habit got a checkoff in time of the set period:
#             -> startdate + frequency -> periodrange
#             -> if last period remained unchecked:
#                 -> display fail message
#                 -> add streak_count to streak_archive
#                 -> reset streak_count
#                 -> reset period_count
#         """

#         frequency = fetch_habit_frequency(name)
#   
## -> imp;ementiert in der habit class



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
    # Alternativ: check lowest streak rate in last 2 weeks

    # def shorteststreakhabit():
    # """
    # "With which habit did the user struggle the most in den letzten 2 Wochen?" -> wird definiert als: lowest streak durchschnitt.
    # calculate: 
    # NOTES:
    # date.today - start_day = x Tage, 
    # len(streak_archive (if 0 take streak_count (if 0 take len(period_count)))
    # -> tage / number_of_streaks -> niedrigste nummer -> struggled the most.
    # Add all streak_count and streak_archive length, attributes for the lowest number.
    # """
    # ....... erstmal rausgenommen, nicht mehr geschafft... :/ 
 
