import utility

N = int(input("Enter array size:\n"))
A = []

print("Enter an array of integers:")

for i in range(N):
    A.append(int(input("")))
       
S = int(input("Enter element to be searched:\n"))

return_val = utility.search(A,N,S)

print(return_val)