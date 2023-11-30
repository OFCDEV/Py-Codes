#Write a code to find distnce between two points
import math
x1 = float(input('Enter the 1st coordinate of x: '))
x2 = float(input('Enter the 2nd coordinate of x: '))
y1 = float(input('Enter the 1st coordinate of y: '))
y2 = float(input('Enter the 2st coordinate of y: '))

distance = math.sqrt(pow((x2-x1),2)+pow((y2-y1),2))

print(distance)
