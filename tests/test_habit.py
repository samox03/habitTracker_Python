import pytest
from functionality.db import connect_db, habit_exists
from functionality.habit import Habit

#unfortunately due tuo the lack of time until the deadline the testing setup is just noted for the first tries....

@pytest.fixture(scope='module')

# TODO: Macht das Sinn die db_connection zu testen, wenn man ein Error management in der Funktion hat?
def test_connect_db():
    print('\n*****STARTING_THE_TEST_SETUP*****\n')
    db = connect_db("test.db")
    print("Created temporary test.db for testing purpose.\n")
    print("Initiating tests...\n")
    yield db
    print("\nConnection with test database will be closed now...\n")
    db.close()
    print("DB connection successfully closed.")
    import os
    os.remove("test.db")
    print("\ntest.db file got removed again.")

def test_add_habit(db):
    habit = Habit("coding", "daily", "2024-03-20", database="test.db")
    habit.add()
    assert habit_exists(db, "coding")

def test_change_frequency():
    habit = Habit("coding", "daily", "2024-03-20", database="test.db")
    habit.change_frequency("weekly")
    assert habit.frequency == "weekly"

def test_delete_habit(db):
    habit = Habit("coding", "daily", "2024-03-20", database="test.db")
    habit.delete()
    assert not habit_exists(db, "coding")

# def test_update_analysisdata(db, name, frequency, period_count, streak_count, streak_archive): 
# def test_checkoff_event_handler(db, name):
# def test_longest_streak_given_habit(habit_name):
# def test_longest_streak_all_habits(): 
# def test_get_streak_count(db, name): 
# def test_get_all_streak_counts(db):
# def test_reset_analysisdata(db, name):


