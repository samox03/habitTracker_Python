# habitTracker_Python
Conception and construction of a CRUD habit tracker with some analytical functionality. 
-> Backend + CLI 

## Getting Started

Important: Make sure that Python 3.12 + is installed on your OS.

## Dependencies

- Python 3.12 +
- Pandas
- Tabulate

## Installing
You can download the latest version of Python from [this link](https://www.python.org/downloads/) - Make sure to check "ADD to path" in the Python installer. 

After installing Python, proceed with the installation of the following libraries:

- Pandas
- Tabulate
  
### Packages for running tests

To run the tests, you will need the following packages installed: 
Pytest - For testing functions:

    pip install -U pytest

## How To Run the Program
Upon completing the installation of the necessary dependencies, download the files from this repository and store them in a separate folder. Access your command/terminal interface and navigate to the downloaded folder. Input the following command to run the program:

    python3 main.py

Now the habit tracker CLI will be launched and you can follow the displayed options.


## Running tests

To run the test, navigate to the test folder and type 

    pytest

## Usage
### Add/Remove Habit 
1. Add a habit
2. Remove a habit
3. Back to Main Menu

### Modify/Update a Habit
The user can edit the descriptiption or the habit frequency.

### Check Off a habit
The user is asked to check off a habit at least once in the predefined periodicity. He can do so by selecting the from the main menu.
