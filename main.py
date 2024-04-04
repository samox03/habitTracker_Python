# imports

import questionary as qt
# from tabulate import tabulate
from datetime import date
from functionality import utility
from functionality.analyze import all_habits_list
from functionality.habit import Habit
from functionality.utility import description_change_confirmation, frequency_change_confirmation, habit_delete_confirmation, select_one_habit_from_db, get_startdate
from functionality.db import connect_db, add_habit



# This is the entry point of tha habit analysis tool. Here all the functionality is called that gets defined in the functionality subfolder.

# The following will automatically start from beginning:

# Welcome message
print("""
*** Welcome to your habit tracker!***
""")


#  CLI implementation with qustionary
def menu():
    """
    The CLI is intialized with the questionary library to
    offer a good usability for the habit tracker.
    """

 # Shows 6 choices for the user to choose from
    choice = qt.rawselect(
        "What do you want to do? (Use arrow keys)",
        choices=[
            "Create/Delete a Habit",
            "Edit Habit Frequency",
            "Edit Habit Description",
            "Check Off a Habit from the list",
            "See all stored Habits (All or Sort by Frequency)",
            "Analyze your Habits",
            "Exit"
        ]).ask()

# Create or delete a habit
    if choice == "Create/Delete a Habit":
        # user can choose from 3 sub choices
        second_choice = qt.select(
            "Would you like to Create or Delete a Habit?",
            choices=[
                    "Create a Habit",
                    "Delete a Habit",
                    "Back to Main Menu"
                ]).ask()
        
        if second_choice == "Create a Habit":
            # db = connect_db()
            habit_name = utility.habit_name()
            print("print:", habit_name)
            habit_description = utility.habit_description()
            print("print:", habit_description)
            new_frequency = utility.habit_frequency()
            print("print:", new_frequency)
            start_date = get_startdate()
            print("print:", start_date)
            habit = Habit(habit_name, habit_description, new_frequency, str(start_date))
            habit.add()
            print("Yay! You started a new Habit track! | Habit: " +habit_name, "| Description: " +habit_description, "| Frequency: " +new_frequency, "| Tracked since: " +str(start_date))
            menu()

            # TODO: next line should be deleted:
            # add_habit(habit_name, habit_description, new_frequency, start_date)


        elif second_choice == "Delete a Habit":
            try:
                 habit_name = select_one_habit_from_db()
            # throw ValueError if db is empty
            except ValueError:  
                print("\nThe habit database is empty - please create a habit first.\n")
            else:
                habit = Habit(habit_name)
                if habit_delete_confirmation(habit_name):
                    habit.remove()
                else:
                    print("\nNo such habit in the database :/ \n")

            menu()

        elif second_choice == "Back to Main Menu":
            menu()
        
# Edit a habits frequency           

        elif second_choice == "Edit Habit Frequency":
            try:
                 habit_name = select_one_habit_from_db()
            # throw ValueError if there are no habits in the database
            except ValueError: 
                print("\nThe database is empty - please create a habit first.\n")
            else:
                new_frequency = utility.habit_frequency()
                if frequency_change_confirmation():
                    habit = Habit(habit_name, new_frequency)
                    habit.change_frequency()
                else:
                    print(f"\nThe frequency of {habit_name} was not updated.\n")


        elif second_choice == "Edit Habit Description":
            try:
                habit_name = select_one_habit_from_db()
                 # throw ValueError if there are no habits in the database
            except ValueError: 
                print("\nThe database is empty - please create a habit first.\n")
            else:
                new_description = utility.habit_description()
            if description_change_confirmation():
                habit = Habit(habit_name, new_description)
                habit.change_description()
                
        # elif second_choice == "Check Off a habit from the list":
        #     try:
                
        # # add content

        elif second_choice == "See all stored habits (All or Sorted by Periodicity)":
        # user can choose from 3 sub choices
            second_choice = qt.select(
              "Please specify the intended habit selection:",
                choices=[
                    "List ALL habits",
                    "List all DAILY habits",
                    "List all WEEKLY habits"
                    "Back to main menu"
                ]).ask()
        
            if second_choice == "List ALL habits":
                # list all habits from db
                all_habits_list()
                menu()
            
            elif second_choice == "List all DAILY habits":
                get_habits_by_frequency("daily")

            elif second_choice == "List all WEEKLY habits":
                get_habits_by_frequency("weekly")
        #             # add content
                
            elif second_choice == "Back to Main Menu":
                menu()
            
  
        
        # elif choice == "Analytics":

        # # add content
            
        # elif second_choice == "Back to Main Menu":
        #     menu()


    elif choice == "Exit":
        # Goodbye message
        print("\nCiao my friend! - Stay successfull with keeping track on your habits :)")  
        exit()  # exit() completely exits the program


# Initial call to start the habit analyzer
menu()  