#lambda,map,filter
cube=lambda x: x**3
add= lambda x,y: x+y
print(cube(2))
print(add(2,3))
mark=[40,30,80,95,70]
updated_mark=list(map(lambda x:x+5,mark))
print(updated_mark)
l=[-1,-3,4,6,-10]
l_n=list(map(abs,l))
print(l_n)
x=[1,2,3,4,5,6,7,8,9,10]
y=list(filter(lambda x: x%2 ==0,x))
print(y)
s={1,2,3,4,5,6}
print(s)
s1=set()
print(s1)
str='ITER'
st=set(str)
print(st)
set1={1,2,3,5,'iter'}
for i in set1:
    print(i)
s3={1,2,3,4,5}
s4={3,4,5,6}
print(s3.union(s4))
print(s3|s4)
print(s3.intersection(s4))
print(s3.symmetric_difference(s4))
