character_name = "srinivas"
character_age = "25"
print("there was a guy named "+ character_name)
print("his age is "+ character_age)


=======================================================

x = list(range(1,6))
print(x)
print(x[0])
print(x[1:3])
print(x[-2])
print(x[-2::-2])
print(x[1:-1])
x.append(10)
print(x)
x.remove(10)
print(x)
if x.index(5)>5:
 x.remove(5)
 print(x)
print(x.pop())
print(x)


====================================================================






x = [1,2,3,4,5,6,7,8]
print(x)
new_list = [i*i for i in x if i%2 != 0]
print(new_list)

x = [2,3,4,2,5,6,3]
print(x)
unique_list = list(set(x))
print(unique_list)

=================================================================================

#from re import I
#Task1
import math
import functools
import operator
numbers = list(range(1,101))
print(numbers)
#for p in range(2,101):
new_list = [i for i in range(2,101) if all(i%x != 0 for x in range(2,i))]
  #result = list(filter(lambda x : (p%x != 0), numbers))
print(new_list)
print(functools.reduce(operator.add, new_list))
print(functools.reduce(lambda x,y:x+y, new_list))


=================================================================================

#shallow
import copy
numbers = [2,3,4]
new_list = copy.copy(numbers)
print(new_list)
new_list[1] = 8
print(numbers)
print(new_list)
print(id(numbers))
print(id(new_list))
==================================================================================================




#dicttsk2
employee1 = {'name':'alice', 'salary':50000, 'department':'sales'}
employee2 = {'name':'bob','salary':60000, 'department':'sales'}
employees = {'employee1':employee1,'employee2':employee2}
x = employee1.get('salary')
y = employee2.get('salary')
z = x+y
my_dict = {'sales':z,'marketing':'none','engineering':'none'}
z = my_dict.values()
print(my_dict)

#new_dict['sales']

======================================================================================



#task2
l = ['sunaina', 'srinivas', 'roopesh',
'sunaina', 'Tarun', 'sunaina', 'tarun']
l = [item.upper() for item in l]
l1 = list(set(l))
print (l1)
