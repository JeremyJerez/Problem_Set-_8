# Python_Intro
# Problem Set 8
#A series of exercises for CS50 hands-on projects
"""
This one's my approach to the "Seasons of Love" problem
"""
from datetime import date
import sys
import re
import inflect

X = inflect.engine()

def main():
    Birthday = input("Date of Birth: ")
    try:
        year, month, day = check_Birthday(Birthday)
    except:
        sys.exit("Invalid date")
    BirthDate = date(int(year), int(month), int(day))
    ActualDate = date.today()
    Diff = ActualDate - BirthDate
    Total_Minutes = Diff.days * 24 * 60
    Output = X.number_to_words(Total_Minutes, andword='')
    print(Output.capitalize() + " minutes")


def check_Birthday(Birthday):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", Birthday):
        year, month, day = Birthday.split("-")
        return year, month, day


if __name__ == "__main__":
    main()
