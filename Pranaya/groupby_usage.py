# Count the number of names for each first letter. 
# Using Groupby names = ['sunaina', 'pranaya', 'srinivas', 'tarun raj', 'tarun ghanta']

#import groupby from itertools
from itertools import groupby
names = ['sunaina', 'pranaya', 'srinivas', 'tarun raj', 'tarun ghanta','sridevi']
names.sort() #sorted('pranaya','srinivas','sunaina','tarun ghanta','tarun raj')
g = groupby(names, lambda name:name[0] ) #grouping by first letters of a name 
print ([(key, len(list(value))) for key, value in g])