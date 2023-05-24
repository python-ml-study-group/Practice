'''Write a function that takes a 
dictionary as input and returns the 
key with the maximum value.'''

my_dict = {'a': 10, 'b': 5, 'c': 15, 'd': 7, 'f':25}  #creates dictionary

def get_key_of_max_value(dictionary): #defines the function to get the key of max value from the dictionary

    max_value = max(dictionary.values())  # Find the maximum value in the values of the dictionary
    for key, value in dictionary.items():
        if value == max_value:
          return key                      #returns the key if the value in the dictionary matches with the max_value

key_for_max_value = get_key_of_max_value(my_dict) 
print("Key with maximum value:", key_for_max_value)