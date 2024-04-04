
"""
This module takes care of the analysis processes.
Setup of all required actions and validations for a checkoff-event.
"""


from functionality.db import connect_db, connect_database, fetch_habits_to_choose_from




def all_habit_list():
    """Display all habits from the database"""

    try:
        import sqlite3
        import datetime
        import time
        from datetime import datetime, timedelta

        connect_db()

# # TODO: Initialize the sqlite db called main.db
#         sqliteConnection = sqlite3.connect('main.db.sqlite3')
#         conn = sqliteConnection.cursor()

        # Fetch all habits from the habit database
        command = """SELECT * FROM habit_coredata"""
        conn.execute(command)
        records = conn.fetchall()
        print("Here you see a list of ALL stored habits in the database:  ", len(records))
        print("\n")

        # Print each row in the records
        for row in records:
            print(row)

        sqliteConnection.commit()
        conn.close()

    except sqlite3.Error as error:
        print("Unable to read data from the database:", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()






# TODO get frequency of the checkoff_habit

    # -> unnoetig, es kann einfach gleich der library befehl genutzt werden. 
    # def checkoff_date(db, self.name):
    #     """
    #     :param db: connected sqlite database
    #     :param name: name of the habit that is requested to be checked off
    #     :param date_checkoff_try: a variable only for shortterm use of the calculation.
    #     :return: date of the day
    #     """
    #     date_checkoff_try = datetime.now()
    #     return name.date_checkoff_try

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

            # If no checkoff exists, add the new date to the period_counter list
            period_count.append(current_date)
            print("Cool another period success for this habit!")
            return True


# TODO: Delete Example:
# Example usage
startdate = datetime.strptime("2022-10-10", "%Y-%m-%d")
period_counter = []
new_date = datetime.now()

if check_weekly_checkoff(startdate, period_counter, new_date):
    print("New checkoff added successfully!")
else:
    print("Checkoff already exists in the current period!")


########################################################################
    


def streak_control(db, name, frequency, period_counter, streak_counter, streak_archive):

    """
    Checks if the user reached a 2 Weeks streak.
    :param db: connected sqlite database
    :param name: name of the habit
    :param frequency: frequency of the habit
    :param period_counter: list of recent checkoff dates
    :param streak_counter: counts every 2 Weeks streek with 1, gets set 0 if a period is missed.
    :param streak_archive: stores all streaks, also if a missed period reset the streak_counter.              
    """

    if frequency == 'daily':
        if len(period_counter) == 2:
            print(f"Cool! You reached a streak of '{len(period_counter)}' completed periods for the '{name}' habit!")
            streak_counter += 1

    elif frequency == 'weekly':
        if len(period_counter) == 15:
            print(f"Cool! You reached a streak of '{len(period_counter)}' completed periods for the '{name}' habit!")
            streak_counter += 1




# TODO:    def period_checker(db, name, new_checkoff_date, period_counter()):

# TODO:    def increment_streak_counter(db, self.name, date):

# TODO:    def add_streak_counter(db, self.name, self.frequency)




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


