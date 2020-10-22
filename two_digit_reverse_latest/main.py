import utility
num = int(input("Enter a two digit number:\n"))
return_val = utility.reverse(num)
if return_val == -1:
    print("Enter a two digit number!!!")
else:
    print(return_val)