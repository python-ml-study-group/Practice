#Write a function that takes a dictionary as input and returns the key with the maximum value.
ages = {
    'charan': 23,
    'sweety': 24,
    'chintu': 22,
    'parth': 20,
    'sree' : 29 
}
max_value = max(ages, key=ages.get)  #the .get() method is used to return the value for a key. 
print(max_value)