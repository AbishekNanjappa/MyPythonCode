def check_leap_year(year):
    result = "Not a leap year"
    if year % 4 == 0 and year % 100 != 0:         
        result = "Leap year"
    elif year % 400 == 0:
        result = "Leap year"
    return result
    