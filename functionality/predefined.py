import sqlite3
from sqlite3 import Error

def tablecreation():
    """
    Create the 'test.db' table in the SQLite database file.
    """
    # sqliteConnection = None

    try:
        sqliteConnection = sqlite3.connect('test.db')
        conn = sqliteConnection.cursor()
        print("Connected to SQLite")

        command = """CREATE TABLE IF NOT EXISTS habits(
            'name' TEXT NOT NULL PRIMARY KEY,
            'description' TEXT,
            'frequency' TEXT NOT NULL,
            'start_date' DATE NOT NULL,
            'period_count' TEXT,
            'streak_count' INTEGER DEFAULT 0,
            'streak_archive' TEXT
        )"""

        conn.execute(command)

        # len records of Habits exists
        conn.execute("SELECT * FROM habits").fetchall()

# test TODO: ->delete or apply
        habits_data = [('Workout', 'Care about your body :)', 'Daily', '2024-03-20', ['2024-03-21', '2024-03-22', '2024-03-24', '2024-03-25', '2024-03-26', '2024-03-27', '2024-03-28', '2024-03-29', '2024-03-30', '2024-03-31', '2024-04-01', '2024-04-02', '2024-04-03', '2024-04-04'], 1, 0),
              ('WaterPlants', 'Check the health of the plants', 'Weekly', '2024-01-01', ['2024-04-14', '2024-04-19'], 3, 2),
              ('TidyUp', 'Bringing away old glass, cleaning the place', 'Weekly', '2024-02-14', ['2024-03-28', '2024-04-04'], 1, 3),
              ('EatFruits', 'Eating daily some vitamins', 'Daily', '2024-03-01', ['2024-03-04', '2024-03-05', '2024-03-06', '2024-03-07', '2024-03-08', '2024-03-09', '2024-03-10', '2024-03-11', '2024-03-16', '2024-03-17', '2024-03-18', '2024-03-19', '2024-03-20'], 1, 0),
              ('Studying', 'Reaching one study goal a week', 'Weekly', '2024-01-29', ['2024-03-06', '2024-03-10'], 5, 4)
              ]

        conn.executemany(
             "INSERT OR REPLACE INTO habits ('name', 'description', 'frequency', 'start_date', 'period_count', 'streak_count', 'streak_archive') VALUES (?,?,?,?,?,?,?)", habits_data)

        sqliteConnection.commit()
        print("Successfully populated 'habits' table with initial data")

#test ende

        records = conn.fetchall()
        print("Total habits are:  ", len(records))
        print("Succeed to create table")

        sqliteConnection.commit()
        conn.close()

    except sqlite3.Error as error:
        print("Error creating the test db data:", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("\n")
            # print('SQLite connection is closed')

def predefinedhabits():
        """
        Insert 5 predefined habits into the 'test.db' table.
        """
        import sqlite3
        from datetime import datetime

        sqliteConnection = sqlite3.connect('test.db')
        conn = sqliteConnection.cursor()

        # name, description, frequency, start_date, period_count, streak_count, streak_archive

        habits = [('Workout', 'Care about your body :)', 'Daily', '2024-03-20', ['2024-03-21', '2024-03-22', '2024-03-24', '2024-03-25', '2024-03-26', '2024-03-27', '2024-03-28', '2024-03-29', '2024-03-30', '2024-03-31', '2024-04-01', '2024-04-02', '2024-04-03', '2024-04-04'], 1, 0),
              ('WaterPlants', 'Check the health of the plants', 'Weekly', '2024-01-01', ['2024-04-14', '2024-04-19'], 3, 2),
              ('TidyUp', 'Bringing away old glass, cleaning the place', 'Weekly', '2024-02-14', ['2024-03-28', '2024-04-04'], 1, 3),
              ('EatFruits', 'Eating daily some vitamins', 'Daily', '2024-03-01', ['2024-03-04', '2024-03-05', '2024-03-06', '2024-03-07', '2024-03-08', '2024-03-09', '2024-03-10', '2024-03-11', '2024-03-16', '2024-03-17', '2024-03-18', '2024-03-19', '2024-03-20'], 1, 0),
              ('Studying', 'Reaching one study goal a week', 'Weekly', '2024-01-29', ['2024-03-06', '2024-03-10'], 5, 4)
              ]
        
#    habits = [('Workout', 'Care about your body :)', 'Daily', '2024-03-20', ['2024-03-21', '2024-03-22', '2024-03-24', '2024-03-25', '2024-03-26', '2024-03-27', '2024-03-28', '2024-03-29', '2024-03-30', '2024-03-31', '2024-04-01', '2024-04-02', '2024-04-03', '2024-04-04'], 1, 0),
#               ('WaterPlants', 'Check the health of the plants', 'Weekly', '2024-03-01', ['2024-03-06', '2024-03-10', '2024-03-18', '2024-03-25', '2024-03-30', '2024-04-09', '2024-04-14', '2024-04-19'], 1, 2),
#               ('TidyUp', 'Bringing away old glass, cleaning the place', 'Weekly', '2024-02-14', ['2024-02-20', '2024-02-25', '2024-03-01', '2024-03-06', '2024-03-12', '2024-03-16', '2024-03-28', '2024-04-04'], 1, 3),
#               ('EatFruits', 'Eating daily some vitamins', 'Daily', '2024-03-01', ['2024-03-01', '2024-03-02', '2024-03-03', '2024-03-04', '2024-03-05', '2024-03-06', '2024-03-07', '2024-03-08', '2024-03-09', '2024-03-10', '2024-03-11', '2024-03-16', '2024-03-17', '2024-03-18', '2024-03-19', '2024-03-20'], 0, 0),
#               ('Studying', 'Reaching one study goal a week', 'Weekly', '2024-01-29', ['2024-01-29', '2024-02-05', '2024-02-10', '2024-02-16', '2024-02-23', '2024-02-29', '2024-03-06', '2024-03-10'], 0, 4)
#               ]


        conn.executemany(
            "INSERT OR REPLACE INTO habits ('name', 'description', 'frequency', 'start_date', 'period_count','streak_count','streak_archive') VALUES (?,?,?,?,?,?,?)",
            habits)

        sqliteConnection.commit()
        print("Successfully written 5 habits to the database")

        conn.close()
        sqliteConnection.close()

tablecreation()
predefinedhabits()