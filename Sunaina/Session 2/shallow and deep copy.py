
"""Explain Shallow copy and deep copy.
What is the difference between them? Give an exmaple"""


# Shallow copy
import copy

original_list = [1, 2, [3, 4]]

# Create a shallow copy of the original list using the copy() method
shallow_copy = copy.copy(original_list)

# Append 5 to the nested list in the shallow copy
shallow_copy[2].append(5)

# Print the original_list to the console
print(original_list)

# Print the shallow_copy to the console
print(shallow_copy)


# Deep copy
original_list = [1, 2, [3, 4]]

# Create a deep copy of the original list using the deepcopy() method
deep_copy = copy.deepcopy(original_list)

# Append 5 to the nested list in the deep copy
deep_copy[2].append(5)

# Print the original_list to the console
print(original_list)

# Print the deep_copy to the console
print(deep_copy)
