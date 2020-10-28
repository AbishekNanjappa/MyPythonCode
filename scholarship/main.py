import utility
stud_type = input("Enter stdent type:\n")
average = int(input("Enter average marks:\n"))
return_val = utility.get_scholarship(stud_type,average)
print(return_val)