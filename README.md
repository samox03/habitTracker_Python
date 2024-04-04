# A Habit Tracker CLI Tool build with Python
Conception and construction of a CRUD habit tracker with some analytical functionality. 
-> Backend + CLI 

# Functionality

The core functionality of the habit tracker are:

- Add habit
- Remove habit
- Add a description of the habit
- Define the tracking frequency of habits (Daily or weekly)
- Checkoff a habit once it is done for its frenquence
- get a reminder if a habid period got missed
- get some congratulation if a habit successfully got tracked for 2 weeks

The tracker allows some analytical actions like:

- View all habits from the DB and its core data
- View all habits from the DB specified by a certain linked periodicity
- View the longest streak of all habits
- return the longest streak for a given habit

## Getting Started

Make sure Python 3.12 + is installed on your OS.

## Dependencies

- Python 3.12 +
- Questionary
- sqlite3 (already included in the python package)
- datetime

## Installing
You can download the latest version of Python from [this link](https://www.python.org/downloads/) - Make sure to check "ADD to path" in the Python installer. 

After installing Python, proceed with the installation of the following libraries:
- Questionary
  
	pip install questionary
  
- datetime
	pip install datetime
  
### Testing
To ensure the validity of the habit tracker, its habit tracking components and the analytics module get tested by a unit test suite.
To run the tests, you will need the following packages installed: 
Pytest - For testing functions:

    pip install -U pytest

## How To Run the Program
Upon completing the installation of the necessary dependencies, download the files from this repository and store them in a separate folder. Access your terminal and navigate to the downloaded folder. Input the following command to run the program:

    python3 main.py

Now the habit tracker CLI will be launched and you can follow the displayed options in the CLI.

## Database
There are 5 predefined habits that the user can delete later.

## Running tests

To run the test, navigate to the test folder and type 
    
    pytest

## Usage
### Add/Remove Habit 
Follow the instructions on your CLI after starting the programm. For navigation use the arrow-keys of your keyboard. Confirm with the enter-key.

### Modify/Update a Habit
The user can edit the descriptiption or the habit frequency.

### Check Off a habit
The user is asked to check off a habit at least once in the predefined periodicity. He can do so by selecting this option from the main menu. A habit can just be checked off once in a period. The checking off of a habit gets registered by the period_counter by +1. The period counter resets to 0 if a habit gets missed in the preset period. In the period_archive the highest value of the period counter gets stored.

### Show Habits 
Shows a table of all the stored habits along with their information of Name, Description, Periodicity.

### Analysis
The following operations can get analysed by the habit tracker:
  - return a list of all currently tracked habits.
	- return a list of all habits with the same frequency (daily, weekly).
	- return the longest run streak of all defined habits (→ checks for highest nr in the streak_count among all habits)
	- return the longest streak for a given habit (→ checks the streak_archive of a given habit)

