"""
This module manages and defines user inputs that request a further 
definition or confirmation. 
Example: The user is asked for confirmation of a deletion action or the habit name gets checked 
due to formal naming restrictions.
Also some simple database requests are defined here, 
therefor some functions from the db module are imported here.
The confirmation functions are implemented with the questionary library.

The implementation of these functions in a seperate filestructure aims to increase the 
reusability and readability of the code.
"""

import questionary as qt
from functionality.db import connect_db, fetch_habits
from datetime import date


def habit_name():
    """
    Asks the user to enter the habit name and validates it.
    
    :return: Returns the name of the habit provided by the user.
    """

    return qt.text("Please Enter the Name of the Habit you want to track:",
                   validate=lambda name: True if name.isalpha() and len(name) > 1
                   else "Please enter a valid name, no empty spaces or special characters are allowed.").ask().lower()


def habit_description():
    """
    Asks the user to enter a short description of the habit.
    
    :return: Returns the description of the habit provided by the user.
    """
    return qt.text("Please Enter a short description of the Habit you want to track (max. 20 Words):",
                   validate=lambda name: True if 1 <= len(name.split()) <= 20 
                   else "Please try again!").ask().lower()


def get_startdate():
    start_date = date.today()
    return start_date


def fetch_all_habits_to_select_one():
    """
    Displays all habit names from db for the user to choose from.

    :return: Returns the selected habit
    :ValueError: If DB contains no data ValueError is thrown.    
    """

    db = connect_db()

    list_of_all_habits = fetch_habits(db)

    if list_of_all_habits is not None:
        return qt.select("Please Select a Habit",
                         choices=sorted(list_of_all_habits)).ask().lower()
    else:
        raise ValueError("No habit in database. Add a habit first to use this function!")

        


def habit_frequency():
    """
    Asks for a concrete frequency choice.

    :return: Returns the selected habit periodicity
    """
    return qt.select("Please Select Habit Frequency",
                     choices=["Daily", "Weekly"]).ask().lower()


def frequency_change_confirmation():
    """
    Asks for confirmation for a frequency change of a habit.

    :return: Return True if yes else returns False
    """
    return qt.confirm("Changing the frequency of the habit will reset the current period as well as the streak_count, would you like to continue?").ask()


def description_change_confirmation():
    """
    Asks for description for a frequency change of a habit.

    :return: Return True if yes else returns False
    """
    return qt.confirm("Changing the description of the habit will reset the current description. Would you like to continue?").ask()


def habit_delete_confirmation(habit_name_to_delete):
    """
    Requests the user to confirm whether they like to delete the habit or not.
    :return: Return True if yes else returns False

    """
    return qt.confirm(f"Would you like to delete '{habit_name_to_delete}' habit from the database?").ask()


def show_frequency_choices():
    """
    Asks the user to specify which habits shall be shown.
    :return: Returns the chosen action

    """
    choice = qt.select("Would you like to view all habits or sort habit by periodicity?",
                       choices=[
                           "View All Habits",
                           "View Daily Habits",
                           "View Weekly Habits",
                           "Back to Main Menu"
                       ]).ask()
    return choice


def analytics_choices():
    """
    Requests the user to select from the list of provided analytical choices.
    """
    choice = qt.select("Please choose an option:",
                       choices=[
                        #    "View All Habit's Streaks",
                           "Show the longest streak count from all habits",
                           "Show the longest streak count from a specific habit",
                           "Back to Main Menu"
                       ]).ask()
    return choice