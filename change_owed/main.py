import utility

five_dollar_coins_available = int(input("Enter the number of $5 coins available:\n"))
one_dollar_coins_available = int(input("Enter the number of $1 coins available:\n"))
amount = int(input("Enter the amount:\n"))

return_val = utility.change_owed(five_dollar_coins_available,one_dollar_coins_available,amount)

if return_val == -1:
    print("NP")
else:
    print(return_val)