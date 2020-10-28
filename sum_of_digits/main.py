import utility
N = int(input("Enter the value of N:\n"))
if utility.sum_of_digits(N) == -1:
    print("Enter a positive integer!!!")
else:
    print(utility.sum_of_digits(N))