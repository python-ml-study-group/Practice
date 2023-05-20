#import copy module of python for Shallow and deep copy operations
import copy

# Original list
original_list = [1, 2, [3, 4]]

# Shallow copy
shallow_copy = copy.copy(original_list)

# Deep copy
deep_copy = copy.deepcopy(original_list)

# Modifying the nested list in shallow copy
shallow_copy[2].append(5)

# Modifying the nested list in deep copy
deep_copy[2].append(6)

print("Original List:", original_list)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)
