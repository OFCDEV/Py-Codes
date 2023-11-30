def checkMax(a,b,c):
    if a>b and a>c:
        print("A is greater.")
    elif b>a and b>c:
        print("B is greater.")
    else:
        print("C is greater.")

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

checkMax(a,b,c)
