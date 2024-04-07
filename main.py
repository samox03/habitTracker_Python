# imports

import questionary as qt
#  from tabulate import tabulate
from datetime import date
from functionality import utility
from functionality.analyze import checkoff_event_handler, longest_streak_all_habits, longest_streak_given_habit
from functionality.db import  connect_db, all_habits_list, get_habits_by_frequency
from functionality.habit import Habit
from functionality.predefined import predefinedhabits, tablecreation
from functionality.utility import frequency_change_confirmation, habit_delete_confirmation, fetch_all_habits_to_select_one, get_startdate



# This is the entry point of tha habit analysis tool. Here all the functionality is called that gets defined 
# in the functionality subfolders.



db_name = "main.db"
conn = connect_db(db_name)

if conn is not None:
    print(f"Connected to database: {db_name}")

    # Perform operations with your database connection
    # Example: Get all habits from the database
    all_habits_list()
else:
    print("Connection to the database failed.")

tablecreation()
predefinedhabits()


# The following defines the CLI userflow:

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
        "What do you want to do?",
        choices=[
            "Create/Delete a Habit",
            "Edit Habit Frequency",
            # "Edit Habit Description",
            "Check Off a Habit from the list",
            "See all stored Habits (All or Sort by Frequency)",
            "Analyze your Habits",
            "Exit"
        ]).ask()

    # Create or delete a habit
    if choice == "Create/Delete a Habit":
        # User can choose from 3 sub choices
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
            habit_description = utility.habit_description()
            new_frequency = utility.habit_frequency()
            start_date = get_startdate()
            habit = Habit(habit_name, habit_description, new_frequency, str(start_date))
            habit.add()
            print("Yay! You started a new Habit track! | Habit: " +habit_name, "| Description: " +habit_description, "| Frequency: " +new_frequency, "| Tracked since: " +str(start_date))
            menu()


        elif second_choice == "Delete a Habit":
            try:
                 habit_name = fetch_all_habits_to_select_one()
            # throw ValueError if db is empty
            except ValueError:  
                print("\nThe habit database is empty - create a habit first!\n")
            else:
                habit = Habit(habit_name)
                if habit_delete_confirmation(habit_name):
                    habit.remove()
                else:
                    print("\nNo such habit in the database :/ \n")

            menu()


        # Edit a habits frequency           
        elif second_choice == "Edit Habit Frequency":
            try:
                 habit_name = fetch_all_habits_to_select_one()
            # throw ValueError if there are no habits in the database
            except ValueError: 
                print("\nThe database is empty - create a habit first!\n")
            else:
                new_frequency = utility.habit_frequency()
                if frequency_change_confirmation():
                    habit = Habit(habit_name, new_frequency)
                    habit.change_frequency()
                else:
                    print(f"\nThe frequency of {habit_name} was NOT updated.\n")
            menu()

    
        # elif second_choice == "Edit Habit Description":
        #     try:
        #         habit_name = fetch_all_habits_to_select_one()
        #          # throw ValueError if there are no habits in the database
        #     except ValueError: 
        #         print("\nThe database is empty - create a habit first!\n")
        #     else:
        #         new_description = utility.habit_description()
        #     if description_change_confirmation():
        #         habit = Habit(habit_name, new_description)
        #         habit.change_description()
                
        elif second_choice == "Check Off a Habit from the list":
            try: 
                habit_name = fetch_all_habits_to_select_one()
                checkoff_event_handler(habit_name)

            except ValueError:  # ValueError is raised when there are no habits in the database
                print("\nPlease first create a habit to use the check-off function\n")

                
        # TODO: add content

        elif choice == "See all stored Habits (All or Sort by Frequency)":
        # user can choose from 3 sub choices
            second_choice = qt.select(
              "Please specify the intended habit selection:",
                choices=[
                    "List ALL habits",
                    "List all DAILY habits",
                    "List all WEEKLY habits",
                    "Back to Main Menu"
                ]).ask()
        
            if second_choice == "List ALL habits":
                # list all habits from db
                all_habits_list()
                menu()
            
            elif second_choice == "List all DAILY habits":
                get_habits_by_frequency("daily")
                menu()

            elif second_choice == "List all WEEKLY habits":
                get_habits_by_frequency("weekly")
                menu()
                
            elif second_choice == "Back to Main Menu":
                menu()
            
        
        elif choice == "Analyze your Habits":
            second_choice = utility.analytics_choices()
            if second_choice == "Show the longest streak count from all habits":
                try:
                    # Gives the highest nr of all streak counts and streak archives.
                    highest_streak_count, habit_name = longest_streak_all_habits()
                    print(f"You succeeded the most streaks in a row [{highest_streak_count}] with the habit {habit_name}")
                
                except ValueError:  # ValueError is raised when there are no habits in the database
                    print("\nPlease first create habits and tracking data before trying to analyze them ;)\n")



            elif second_choice == "Show the longest streak count from a specific habit":
                try:
                    habit_name = fetch_all_habits_to_select_one()
                    longest_streak = longest_streak_given_habit(habit_name)
                    print(f"The longest streaks in a row of the habit", {habit_name}, "are:", {longest_streak} )

                except ValueError:  # ValueError is raised when there are no habits in the database
                    print("\nPlease first create habits and tracking data before trying to analyze them ;)\n")


            #deactivated due to lack of time :/
            #elif second_choice == "With which habit did I struggle the most in the last streak period?":
                    # def shorteststreakhabit()
                    # print("The shortest streak success is documented for the habit:", {habit_name} )


            elif second_choice == "Back to main menu":
                menu()        
               

         
    elif choice == "Exit":
        # Goodbye message
        print("\nCiao my friend! - Stay successfull with keeping track on your habits! :)")  
        exit()  # exit() completely exits the program


# Initial call to start the habit analyzer
menu()  