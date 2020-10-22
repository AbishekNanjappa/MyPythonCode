def change_owed(five_dollar_coins_available,one_dollar_coins_available,amount): #simplify th logic
    five_dollar_coins_required = 0
    one_dollar_coins_required = 0
    flag = 0
    result = (-1,-1)
    if amount > 5*five_dollar_coins_available + one_dollar_coins_available:
        flag = 1
    else:
        while amount > 0:
            if amount >= 5:
                if five_dollar_coins_available > 0:
                    amount -= 5
                    five_dollar_coins_available -= 1
                    five_dollar_coins_required += 1
            elif amount < 5 and amount >= 1:
                if one_dollar_coins_available > 0:
                    amount -= 1
                    one_dollar_coins_available -=1
                    one_dollar_coins_required += 1 
    if flag == 0:
        result = (five_dollar_coins_required,one_dollar_coins_required)
    return result 

    
   