#importing copy module of python 
import copy

# actual  list with mutable object inside the list
l1_list = [1, 2, [3, 4]]

# doing a normal copy
sh_copy = copy.copy(l1_list)

# Deep copy
dep_copy = copy.deepcopy(l1_list)

# Modifying the nested list in shallow copy
sh_copy[2].append(5)

# Modifying the nested list in deep copy
dep_copy[2].append(6)

print("Original List:", l1_list)
print("Shallow Copy:", sh_copy)
print("Deep Copy:", dep_copy)