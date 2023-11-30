def cum(lst):
    new_lst=[]
    sum=0
    for i in lst:
        if i not in list:
            sum = sum+1
            new_lst.append(sum)
    return new_lst
def main():
    l = eval(input('Enter a list:'))
    new_l = cum(lst)
    print('Cummulative list =',new_l)
main()
