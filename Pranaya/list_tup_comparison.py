#How will u implement comparison in list, tuple. what are the differences
#can't compare two different data types
a = [1, 2, 3, 4]
b = (2, 3, 4)

#using == operator
if a == list(b):#using list() to convert tuple to a list
    print("a and b are equal")
else:
    print("a and b are not equal")

#using < operatot
if a < list(b):
    print("a is less than b")
else: 
    print("a is greater than b")
