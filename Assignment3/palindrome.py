def reverse(n):
    rev = 0
    d=0
    dup=n
    while(n>0):
        d=n%10
        rev = rev*10+d
        n=n//10
    print(rev)
    if(rev == dup):
        print("Palindrome.")
    else:
        print("Not")
n = int(input('Enter the num u want check: '))
reverse(n)
