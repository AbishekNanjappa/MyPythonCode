def main():
    n1 = n2 = n3 = 0
    n = [n1,n2,n3]
    print("Enter three numbers")
    for i in range(3):
        n[i] = int(input(""))
    get_list(n)
    greatest_num(n)

def greatest_num(n):
    greatest_number = n[0]
    for i in range(3):
        if n[i] > greatest_number:
            greatest_number = n[i]
    print("Greatest number = ",greatest_number)

def get_list(n):
    print("Entered list: " , end = "")
    print(n)

main()
