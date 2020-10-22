import utility
num = int(input("Enter a three digit number:\n"))
return_val = utility.three_digit_reverse(num)
if return_val == -1:
    print("Enter a three digit number")
else:
    print(return_val)