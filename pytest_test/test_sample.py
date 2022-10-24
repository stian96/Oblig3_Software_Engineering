def isLeapYear(year):
    """
    A function that takes a year as a parameter and
    decides if it´s a leap year or not.
    """
    leap_year = True
    not_leap_year = True

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return leap_year
    elif (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0):
        return not_leap_year


# Tests to find out if a year is a leap year.
def test_if_year_is_divisible_with_four_but_not_hundred():
    year = 2004
    assert isLeapYear(year)


def test_if_year_is_divisible_with_four_hundred():
    year = 2000
    assert isLeapYear(year)


# Tests to find out if a year is not a leap year.
def test_if_year_is_not_divisible_with_four():
    year = 1995
    assert isLeapYear(year)


def test_if_year_is_divisible_with_hundred_but_not_four_hundred():
    year = 1700
    assert isLeapYear(year)










