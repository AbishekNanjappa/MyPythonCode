import utility
N = int(input("Enter the value of N:\n"))
List = utility.rev_order(N)
for i in range(len(List)):
    print(List[i] , end = "")