import utility
N = int(input("Enter the value of N:\n"))
List = utility.rev(N)
if List == [-1]:
    print("Entered number is not divisible by N.")
else:
    for i in range(len(List)):
        print(List[i] , end = "")