#Explain Shallow copy and deep copy.What is difference between them?Give an example
#import copy module of python for Shallow and deep copy operations
import copy

# Original list
original_list = [1, 2, [3, 4]]

# Shallow copy
# shallow copying causes changes in both the new as well as in the old list.
shallow_copy = copy.copy(original_list) 

# Deep copy
#a change to the deep copy of a list, the old list doesn’t get affected and vice versa
deep_copy = copy.deepcopy(original_list)

# Modifying the nested list in shallow copy
shallow_copy[2].append(5)

# Modifying the nested list in deep copy
deep_copy[2].append(6)

print("Original List:", original_list)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)