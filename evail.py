#q11
#a=eval(input("Enter the arithmatic:"))
#print(a)

#q12
#def main():
 #   pass
#print(main())

#q13
a = int(input("Enter x1:"))
b = int(input("Enter y1:"))
c = int(input("Enter x2:"))
d = int(input("Enter y2:"))
e = int(input("Enter x3:"))
f = int(input("Enter y3:"))
print(f"Your three points are:{(a),(b)},{(c),(d)},{(e),(f)}")
result = a*(d-f)+c*(f-b)+e*(b-d)
if result ==0:
    print("True")
else:
    print("It is not colinear.")
