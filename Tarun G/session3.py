#Task: count the number of names for each first letter.
from itertools import groupby
names = ['sunaina', 'pranaya', 'srinivas', 'tarun raj', 'tarun ghanta']
names.sort()
g = groupby(names, lambda name:name[0] )

print ([(key, len(list(value))) for key, value in g])

*******************************************************************

from itertools import groupby

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# group the numbers by their value modulo 2
groups = groupby(numbers, lambda x: x % 2)

# iterate over the groups and print them
for key, group in groups:
    print(key, list(group))
    
    
*****************************************************************
numbers = [1, 2, 3, 5, 7, 8, 9, 10]

# group the numbers by whether they are even or odd
groups = groupby(numbers, lambda x: x % 2)

# iterate over the groups and their elements
for key, group in groups:
    print("Group:", key)
    for value in group:
        print("Value:", value)
