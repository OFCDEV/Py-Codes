def perfectNum:
    for i in range(1,n):
        sum = 0
        if(n%i == 0):
            sum = sum+i
        if(sum ==n):
            print("Number is perfect")
        else:
            print("It is not")

n = int(input("Enter the number:"))
