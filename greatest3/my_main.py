import utility
n1 = n2 = n3 = 0
n = [n1,n2,n3]
print("Enter three numbers")
for i in range(3):
    n[i] = int(input(""))
g = utility.greatest_num(n)
print(g)

