import utility
N = int(input("Enter value of N:\n"))
List = utility.first_N_even(N)
for i in range(len(List)):
    print(List[i] , end = " ")