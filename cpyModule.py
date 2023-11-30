#copy module,deep copy and shallow copy
import copy
lst1 =[10,20,30,40,50,[60,70]]
#lst2 =copy.deepcopy(lst1)
lst2 =copy.copy(lst1)
lst2[5][1]=700
print(lst1)
