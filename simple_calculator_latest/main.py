import utility

print("Enter two numbers:")
num_1 = float(input(""))
num_2 = float(input(""))
o = input("Enter an operator (+,-,*,/) :\n")

print("Result = ",utility.calculate(num_1,o,num_2))