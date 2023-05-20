#comaprsion based on order of elements

a = [1, 2, 3, 4]
b = (2, 3, 4)

if a == list(b):
    print("a and b are equal")
else:
    print("a and b are not equal")


# comparison based on the contents of the list/tuple regardless of their order

a = [1, 2, 3, 4]
b = (2, 3, 4, )

if sorted(a) == sorted(list(b)):
    print("a and b are same ")
else:
    print("a and b are not same")
    
    
# using the map function


l = ['sunaina', 'srinivas', 'roopesh', 'sunaina', 'Tarun', 'sunaina', 'tarun']
l = list(map(str.upper, l))
l1 = list(set(l))
print(l1)
