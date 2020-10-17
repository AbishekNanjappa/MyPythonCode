def check_leap_year(year):
    result = "0000"
    if year % 4 == 0:
        result = "Leap year"
    else:
        result = "Not a leap year"
    
    return result
    