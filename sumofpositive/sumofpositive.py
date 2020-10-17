import utility_positive
print("Enter 5 integers:")
#n1 = n2 = n3 = n4 = n5 = 0
#n = [n1,n2,n3,n4,n5]
n1 = int(input(""))
n2 = int(input(""))
n3 = int(input(""))
n4 = int(input(""))
n5 = int(input(""))

positive_sum = utility_positive.sum_of_positive(n1,n2,n3,n4,n5)
print("Sum of positive integers = ", end = "")
print(positive_sum)

