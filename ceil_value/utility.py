def ceil_val(n):
    ceil_value = round(n)    
    ceil_value_new = 0             
    if ceil_value < n:
        ceil_value_new = int(ceil_value + 1)
    else:
        ceil_value_new = ceil_value
    
    return ceil_value_new                        #ceil value after checking if decimal has been rounded to higher or lower integer
    