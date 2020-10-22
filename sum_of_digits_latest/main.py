import utility
num = int(input("Enter a three digit number:\n"))
return_val = utility.sum_of_digits(num)
if return_val == -1:
    print("Enter a three digit number!!!\n")
else:
    print(return_val)
