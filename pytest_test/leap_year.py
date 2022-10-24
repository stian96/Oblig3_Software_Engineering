def isLeapYear(year):
    """ Demonstration of the function in 'test_sample.py'. """
    leap_year = True
    not_leap_year = False

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return leap_year
    elif (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0):
        return not_leap_year


print("True: represents leap year, False: the opposite.")
print("Enter 'q' to quit at any time.")

quit = True
while quit:
    get_year = input("\nEnter a year: ")
    if get_year == 'q':
        quit = False
    else:
        print(isLeapYear(int(get_year)))

