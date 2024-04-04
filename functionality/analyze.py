
"""
This module takes care of the analysis processes.
Setup of all required actions and validations for a checkoff-event.
"""


from functionality.db import connect_db, connect_database, fetch_habits_to_choose_from
import sqlite3



def all_habits_list():
    """Display all habits from the database"""
     
    # connect_db()
    conn = connect_db()

    if conn is None:
        return

    try:
        cursor = conn.cursor()

        # Fetch all habits from the habit database
        command = """SELECT * FROM habit_coredata"""
        conn.execute(command)
        records = cursor.fetchall()
        print("Here you see a list of ALL stored habits in the database:  ", len(records))
        print("\n")

        # Print each row in the records
        for row in records:
            print(row)

        # conn.commit()
        # conn.close()


    except sqlite3.Error as error:
        print("Unable to read data from the database:", error)

    finally: 
        if conn: 
            conn.close()



def get_habits_by_frequency(frequency):
    """Display all habits with either weekly OR daily frequency (depending on user input)"""
    
   # connect_db()
    conn = connect_db()

    if conn is None:
            return

    try:
        cursor = conn.cursor()

        # Fetch all habits from the habit database
        command = """SELECT * FROM habit_tracker WHERE periodicity = ?"""
        conn.execute(command, (frequency,))
        records = cursor.fetchall()
        print("Here you see a list of all stored habits with a ", +frequency, " frequency:  ", len(records))
        print("\n")

        # Print each row in the records
        for row in records:
            print(row)

        else:
            print("Sorry - no habits found with the specified frequency..")

        conn.commit()
        conn.close()

    except sqlite3.Error as error:
        print("Unable to read data from the database:", error)

    finally:
        if conn:
            conn.close()


################################################################
# ANLYSIS FUNCTIONALITY
################################################################
# Required: 
    # db: habit_analysisdata
    # name
    # frequency
    # start_date
    # period_count
    # streak_count
    # streak_archive
            

# TODO: get frequency of the checkoff_habit


    def period_checker(db, name, frequency, period_count):
        """
        Manages the checkoff process while checking if the checkoff date lays in an unchecked period.
        First it checks if the checkoff-frequency is set to weekly or daily.
        It does this by 
        If yes it adds the checkoff date in the period_count attribute. 
        If not, it informs the user.

        :param db: connected sqlite database
        :param new_date: takes the date of checkoff_date() function
        :return: if date lays inside an already checked period -> returns false
        :return: if date lays not inside an already checked period -> returns true and adds the date to the period_count.
        """
    # TODO: Noch undefiniert, dass hier die habit_data von 'name' ausgewaehlt werden.

        if frequency == "weekly":
            # Calculate the start of the current week
            current_date = datetime.now()
            start_of_week = current_date - timedelta(days=current_date.weekday())

            # Check if there was already a checkoff date in the current period
            for date in period_count:
                if start_of_week <= date <= current_date:
                    print("Sorry you already tracked that habit in the current period.")
                    return False
            
            # If no checkoff for the current period exists, add the new date to the period_count list
            period_count.append(current_date)
            print("Cool another period success for this habit!")
            return True

        elif frequency == "daily":
            # Check if there was already a checkoff for that day
            for date in period_count:
                if date.date() == current_date.date():
                    print("Sorry you already tracked that habit in the current period.")
                    return False

            # If no checkoff exists, add the new date to the period_count list
            period_count.append(current_date)
            print("Cool another period success for this habit!")
            return True


# TODO: Delete Example:
# Example usage
startdate = datetime.strptime("2022-10-10", "%Y-%m-%d")
period_count = []
new_date = datetime.now()

if check_weekly_checkoff(startdate, period_count, new_date):
    print("New checkoff added successfully!")
else:
    print("Checkoff already exists in the current period!")


########################################################################
    


def streak_control(db, name, frequency, period_count, streak_count, streak_archive):

    """
    Checks if the user reached a 2 Weeks streak.
    :param db: connected sqlite database
    :param name: name of the habit
    :param frequency: frequency of the habit
    :param period_count: list of recent checkoff dates
    :param streak_count: counts every 2 Weeks streek with 1, gets set 0 if a period is missed.
    :param streak_archive: stores all streaks, also if a missed period reset the streak_count.              
    """

    if frequency == 'daily':
        if len(period_count) == 2:
            print(f"Cool! You reached a streak of '{len(period_count)}' completed periods for the '{name}' habit!")
            streak_count += 1

    elif frequency == 'weekly':
        if len(period_count) == 15:
            print(f"Cool! You reached a streak of '{len(period_count)}' completed periods for the '{name}' habit!")
            streak_count += 1




# TODO:    def period_checker(db, name, new_checkoff_date, period_count()):

# TODO:    def increment_streak_count(db, self.name, date):

# TODO:    def add_streak_count(db, self.name, self.frequency)




# TODO: Initialize the data analysis functions:


# display all habits with a daily frequency:
# def dailyhabitlist():

# display all habits with a weekly frequency:
# def weeklyhabitlist():

# display the habit with the longest streak:
# def habitwithlongeststreak():

# Return the longest run streak for a given habit"""
# def longeststreakgivenhabit():

# Display the habit with the shortest streak success"""
# def shorteststreakhabit():


