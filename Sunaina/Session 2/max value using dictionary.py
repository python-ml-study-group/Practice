""" Write a function that takes a 
dictionary as input and returns the 
key with the maximum value."""

#Dictionary
my_dict = {'a': 3, 'b': 6, 'c': 9, 'd': 12}

# Define a function that takes a dictionary as input and returns the key with the maximum value

def max_key(dictionary):
    max_value = max(dictionary.values())
    for key, value in dictionary.items():
        if value == max_value:
            return key

# Call the function with the given dictionary and assign the returned key to max_key
max_key = max_key(my_dict)

# Print the max_key to the console
print(max_key)


