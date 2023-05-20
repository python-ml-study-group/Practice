character_name = "nagasai"
character_age = "25"
print("there was a guy named "+ character_name)
print("his age is "+ character_age)

##############################


name = "nagasai paidi"
print(name.upper().isupper())
print(len(name))
print(name[0])
print(name.index("i"))
print(name.index("di"))
print(name.replace("paidi", "chowdary"))
x = ["nagasai","tarun"]
print(type(x))
x = "nagasai", "tarun"
print(type(x))
name = "nagasai paidi"
age = "25"
x = {name:age}
print(type(x))


###################################


from math import *
print(-2,5)
print(3+2.5, 3-2.5,3+2.5-4*8)


##################################


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


######################################


x = [1,2,3,4,5,6,7,8]
print(x)
new_list = [i*i for i in x if i%2 != 0]
print(new_list)

x = [2,3,4,2,5,6,3]
print(x)
unique_list = list(set(x))
print(unique_list)



##########################################





numbers = [2,3,2,4,5,6]
names = ["naga", "sai", "tarun", "amogh", "balaji"]
#names.extend(numbers)
print(names)
#names.append("rohit")
print(names)
names.insert(2,"rajesh")
print(names)
names.remove("rajesh")
print(names)
#names.clear()
#print(names.pop())
#print(names)
print(names.index("tarun"))
print(numbers.count(2))
names.sort()
print(names)
#numbers.sort()
print(numbers)
#numbers.reverse()
print(numbers)
new_list = names.copy()
print(new_list)





##################################################




calendar = {"jan":"january", "feb":"febuary", "mar":"march"}
print(calendar["feb"])
print(calendar.get("feb"))
print(calendar.get("apr"))
print(calendar.get("apr", "not a valid key"))

#####################################################




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



########################################################



#task3
import copy
numbers = [1,2,3]
new_list = copy.copy(numbers)  #shallow
print(new_list)
new_list.append(10)
print(new_list)
print(numbers)
print(id(numbers))
print(id(new_list))


##########################################################




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


##########################################################



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


#######################################################


#tuplestask1
a = [1,2,3,4]
b = [2,3,4]
c = tuple(a)
d = tuple(b)
#print(c)
#print(d)
if a == b:
 print('a and b are equal')
else:
 print('a and b are not equal')

####################################################


l1 = ['sunaina', 'srinivas', 'roopesh','sunaina', 'Tarun', 'sunaina', 'tarun']
nagasai = [x.upper() for x in l1]
print(nagasai)
def unique(x):
  return set(x)
#del list

map_result = map(unique, [nagasai])
print(list(map_result))


#######################################################




#del list
l1 = ['sunaina', 'srinivas','tarun raj', 'tarun ghanta']
l3 = []
for item in l1:
  letter = item[0]
  if letter in l3.keys():
     l3[letter] +=1
  else:
    l3[letter]=1
print('final result is:', l3)



#######################################################



