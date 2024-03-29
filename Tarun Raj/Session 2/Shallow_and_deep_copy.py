import copy

# Shallow copy
original_list = [1, 2, [3, 4]]

# Create a shallow copy of the original list using the copy() method
shallow_copy = original_list.copy()

# Append 5 to the nested list in the shallow copy
shallow_copy[2].append(5)

# Print the original_list to the console
print("Original list (shallow copy):", original_list)

# Print the shallow_copy to the console
print("Shallow copy:", shallow_copy)


# Deep copy
original_list = [1, 2, [3, 4]]

# Create a deep copy of the original list using the deepcopy() method
deep_copy = copy.deepcopy(original_list)

# Append 5 to the nested list in the deep copy
deep_copy[2].append(5)

# Print the original_list to the console
print("Original list (deep copy):", original_list)

# Print the deep_copy to the console
print("Deep copy:", deep_copy)
