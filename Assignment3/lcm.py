def lcm(a,b):
    if a == 0 and b == 0:
        return 0
    else:
       return abs(a*b)

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
result = lcm(a,b)
print(result)
