def dup(l):
    list=[]
    for i in l:
        if i not in list:
            list.append(i)
    return list
def main():
    l = eval(input('Enter a list:'))
    new_l = dup(l)
    print(new_l)
main()
