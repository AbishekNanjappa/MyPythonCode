import utility
N = int(input("Enter a natural number N:\n"))
List = utility.first_N_numbers(N)
for i in range(len(List)):
    print(List[i] , end = "")