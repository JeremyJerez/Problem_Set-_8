# Python_Intro
# Problem Set 8
#A series of exercises for CS50 hands-on projects
"""
This one's my Test to the "Seasons of love" problem
"""
from seasons import check_Birthday

def main():
    test_check_birthday()

def test_check_birthday():
    assert check_Birthday("July 3, 1998") == None
    assert check_Birthday("1998-7-3") == None
    assert check_Birthday("1998-07-03") == ("1998", "07", "03")

if __name__ == "__main__":
    main()
