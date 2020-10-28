import utility
N = int(input("Enter a number N:\n"))
List = utility.split_num(N)
for i in range(len(List)):
    print(List[i] , end = "")