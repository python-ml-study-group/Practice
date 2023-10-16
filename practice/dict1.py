
d1 = {"userid": "roopesht", "password": "1221413", "key": "1234"}

# dictionary comprehension, print the key and value like "key" == "value"
print([k + "==" + v for k, v in d1.items()])

#Print the number of items
print(len(d1))

# What happens if you try to access a key that doesn't exist?
#print(d1["firstname"])

from collections import defaultdict
def default_value():
    return "N/A"

d2 = defaultdict(default_value)
d2["name"] = "Roopesh"
d2["age"] = 30

print (d2)
print(d2["name"])
print(d2["firstname"])