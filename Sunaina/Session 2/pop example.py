
"""What happens if you use Pop() function with a list?"""

#List of cities
cities = ['Toronto', 'Montreal', 'Ottawa']

# Remove and return the last city from the list using the pop() method
last_city = cities.pop()

# Print the last_city to the console
print(last_city)

# Print the updated list of cities after removing the last city
print(cities)

cities = ['Toronto', 'Montreal', 'Ottawa']

# Remove and return the city at index 1 from the list using the pop() method
second_city = cities.pop(1)

# Print the second_city to the console
print(second_city)

# Print the updated list of cities after removing the city at index 1
print(cities)
