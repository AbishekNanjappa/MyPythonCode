def check_leap_year(year):
    result = "0000"
    if year % 4 == 0 and year % 100 != 0:         
        result = "Leap year"
    elif year % 400 == 0:
        result = "Leap year"
    else:
        result = "Not a leap year"
    
    return result
    