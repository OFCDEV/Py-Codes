import math
def area(side1,side2,side3):
    assert side1+side2>side3 and side1+side3>side2 and side2+side3>side1
    s=(side1+side2+side3)/2
    ar=math.sqrt(s*s(s-side1)*(s-side2)*(s-side3))
    return ar
side1=float(input("Enter side1:"))
side2=float(input("Enter side2:"))
side3=float(input("Enter side3:"))
ar(side1,side2,side3)
print('area=',ar)
