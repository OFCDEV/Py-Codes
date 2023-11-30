def reverse(n):
    rev = 0
    d=0
    while(n>0):
        d=n%10
        rev = rev*10+d
        n=n//10
    print(rev)

a = int(input('Enter the num u want to reverse: '))
reverse(a)
