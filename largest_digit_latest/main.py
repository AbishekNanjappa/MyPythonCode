import utility
num = int(input("Enter a three digit number:\n"))
return_val = utility.largest_digit(num)
if return_val == -1:
    print("Enter a three digit number!!!")
else:
    print("Largest digit = ",return_val)