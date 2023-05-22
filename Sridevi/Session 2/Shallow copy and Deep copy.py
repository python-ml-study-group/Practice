'''Explain shallow copy and deep copy
What is the difference between them
Give an example'''



import copy
my_list = [1, 2, [3, 4], [7,8]]  

shallow_copy = copy.copy(my_list)  # Creates a shallow copy using the copy() method

shallow_copy[3].append(2)               #  Appends the value at index 3 of my_list

print(my_list)                       # Prints the my_list

print(shallow_copy)                   # Prints the shallow_copy to the console


# Deep copy
my_list = [1, 2, [3, 4],[7,8]]

deep_copy = copy.deepcopy(my_list)  # Create a deep copy of my_list using the deepcopy() method

deep_copy[3].append(9)              # Appends value at index 3 of my_list

print(my_list)                      # Print the my_list to the console

print(deep_copy)                    # Print the deep_copy to the console