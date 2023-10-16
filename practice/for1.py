# Count the number of times 89 appears in the list
l1 = [89, 87, 78, 34, 89, 90, 91, 87, 88, 89, 34, 12, 24, 34, 90, 34]
# use the count method
print("Using the .count method: ", l1.count(89))

# use a for loop
count = 0
for i in l1:
    if i == 89:
        count += 1
print("Using the for loop : ", count)


# Count the number of times 89 appears in the list
# use the Counter
from collections import Counter
print ("Using the counter: ", Counter(l1)[89])

# Use of most common
# List the top 3 most commonly appeared items
print ("Using the most common: ", Counter(l1).most_common(3))

