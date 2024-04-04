
import sqlite3
from sqlite3 import Error
from datetime import date, timedelta

# The database module setsup the database, creates 2 database tables, and stores and returns data.
# How the data is accessed according to the user input is defined here.


# set up of the db connection
def connect_db(db_name="main.db"):
        """
        create a database connection to the SQLite database
        specified by db_file

        :param db_name: Name of the database to create or connect with (default main.db)
        :return: Returns the database connection
        """

        db = sqlite3.connect(db_name)

        # TODO: Muss dies hier drin stehen oder werden die dann immer wieder auf 0 gesetzt?
        create_tables(db)
  
        
        try:
                conn = sqlite3.connect(db_name)
                return conn
        
        except sqlite3.Error as e:
                print("Connection to database failed: ", e)
                return None

        # return db

def create_tables(db):
        """

        Setup of two database tables habit_coredata and habit_analysisdata:

        1. The habit_coredata table stores static information like:
        habitname, description, frequency, start_date 

        2. The habit_analysisdata table stores information that is needed for 
        the analysis functionality like counting events. The parameters include:
        habitname, start_date, frequency, period_count, streak_count, streak_archive

        :param db: connected sqlite database
        """

        cur = db.cursor()

#create table called habit_coredata with static data
        cur.execute(''' CREATE TABLE IF NOT EXISTS habit_coredata (
                name TEXT PRIMARY KEY,
                description TEXT,
                frequency TEXT,
                start_date DATE
        )''')

#create table called habit_analysisdata with fluid data
        cur.execute(''' CREATE TABLE IF NOT EXISTS habit_analysisdata (
                name TEXT PRIMARY KEY,
                start_date DATE,
                frequency TEXT,
                period_count LIST OF DATES,
                streak_count INT DEFAULT 0,
                streak_archive INT DEFAULT 0,
                FOREIGN KEY (name) REFERENCES habit_coredata(name)
        )''')

        db.commit()

def add_habit(db, name, description, frequency, start_date):
        """ 
        adds a new habit to the db with the input data of the user.

        :param db: connected sqlite database
        :param name: Name of the habit
        :param description: Description of the habit
        :param frequency: Frequency of the habit (daily or weekly)
        :param start_date: Time of habit creation
        """
        # start_date = str(date.today())
        cur = db.cursor()
        cur.execute("INSERT INTO habit_coredata (name, description, frequency, start_date) VALUES( ?, ?, ?, ?)", 
                    (name, description, frequency, start_date))
        db.commit()

def update_analysisdata(db, name, frequency, period_count, streak_count, streak_archive): 
        """
        updates habit tracking data in the db 
        """

        cur = db.cursor()
        cur.execute("INSERT INTO habit_analysisdata VALUES(?, ?, ?, ?, ?, ?)", 
                    (db, name, frequency, period_count, streak_count, streak_archive))
        db.commit()

   

def habit_exists(db, name):
        """ 
        Checks if habit data with the same habit name exists in db

        :param db: Connected sqlite database
        :param name: Name of the habit
        """
        cur = db.cursor()
        query = """SELECT * FROM habit_coredata WHERE name = ?"""
        cur.execute(query, (name,))
        data = cur.fetchone()
        return True if data is not None else False


def delete_habit(db, name):
        """ 
        Deletes habit specified by its name from db 

        :param db: connected sqlite database
        :param name: Name of the habit
        """
        cur = db.cursor()
        cur.execute(f"DELETE FROM habit_coredata WHERE habit == '{name}';")
        db.commit()


def fetch_habits(db):
        """ 
        Gets all habit names from the db and lists them 

        :param db: connected sqlite database
        """
        cur = db.cursor()
        cur.execute("SELECT habit FROM habit_coredata")
        data = cur.fetchall()
        return [i[0].capitalize() for i in set(data)] if len(data) > 0 else None


def update_frequency_alltables(db, name, new_frequency):
        """ 
        resets the frequency of a habit and resets its streak counters 
        :param db: connected sqlite database
        :param name: Name of the habit
        :param new_frequency: new frequency that shall be applied
        """
        cur = db.cursor()
        query = "UPDATE habit_coredata, analysis_data SET frequency = ? WHERE name = ?"
        data = (new_frequency, name)
        cur.execute(query, data)
        db.commit()
        reset_analysisdata(db, name)

# die folgenden 2 Funktionen sollten bereits mit der update_frequency_alltables() funktion abgedeckt sein
# def update_frequency_analysisdata(db, name, new_frequency):
#         """ 
#         resets the frequency of a habit and resets its streak counters 
#         :param db: connected sqlite database
#         :param name: Name of the habit
#         :param new_frequency: new frequency that shall be applied
#         """
#         cur = db.cursor()
#         query = "UPDATE analysis_data SET frequency = ? WHERE name = ?"
#         data = (new_frequency, name)
#         cur.execute(query, data)
#         db.commit()

# # 
# # TODO: This migth be optimized later, if time is left
# def update_frequency(db, name, new_frequency):
#        """
#        Due to the double storage of the frequency attribute,
#        with a frequency update both tables need to be updated.
#        This function combines the update of both databases.
# #      TODO: Does it need a return statement?
#        """
#        update_frequency_coredata(db, name, new_frequency)
#        update_frequency_analysisdata(db, name, new_frequency)
              


# TODO: - check_if_date_is_next_deadline(db, name, date, next_deadline) -> also triggers reminder, stores the period_coounter in the period_archive and resets period_count == 0 of missed




# TODO: - period_count(db, name, ...) -> counts each successfully checked-off period, sets 0 if a period got missed.
# TODO: - streak_archive(db, name, ...) -> stores the quantity of successfully reached habit-periods in a row until the habit gets interrupted.
# TODO: - streak_count() → counts +1 if the period_count counts 2 for weekly habits or 15 for daily habits.


def get_streak_count(db, name):
        """ 
        returns the current streak count of the specified habit 
        """
        cur = db.cursor()
        query = "SELECT streak_count FROM habit_analysisdata WHERE habit = ?"
        cur.execute(query, (name,))
        streak_count = cur.fetchall()
        return streak_count[0][0]


def update_habit_streak_count(db, name, time=None):
        """
        Wenn der streak_checker einen streak registriert hat, wird dieser im streak_count hinzugefuegt.
        """
        cur = db.cursor()
        query = "UPDATE habit_coredata SET streak_count += 1 WHERE name = ?"
        cur.execute(query, (name,))
        db.commit()

def update_habit_period_count(db, name, time=None):
        """
        Wenn der period_checker ein check_off_event fuer die aktuelle Periode registriert,
        wird dieser im period_count als Datum hinzugefuegt.
        """
        cur = db.cursor()
        query = "UPDATE habit_coredata SET period_count = ? WHERE name = ?"
        data = query.append(date.now())
        cur.execute(data, (name,))
        db.commit()

def fetch_habit_frequency(db, name):
        """ returns the specified frequency of a habit """
        cur = db.cursor()
        query = "SELECT frequency FROM habit_coredata WHERE habit = ?"
        cur.execute(query, (name,))
        data = cur.fetchall()
        return data[0][0]


def reset_analysisdata(db, name):
        """
        Accesses the analysis data table, enters the object of {name} and resets the counter data.
        """
        cur = db.cursor()
        query = "UPDATE habit_coredata SET period_count = 0, streak_count = 0 WHERE name = ?"
        cur.execute(query, (name,))
        db.commit()

        print("The tracking data of '{name}' has been deleted due to your last operation.")