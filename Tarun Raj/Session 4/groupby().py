from itertools import groupby

names = ['tarun raj', 'nagasai', 'tarun ghanta', 'srinivas', 'sunaina', 'pranaya','sridevi']

# Define a function to get the first letter of a name
def get_first_letter(name):
    return name[0]

# Sort the names list alphabetically
sorted_names = sorted(names)

# Use groupby to group the names by their first letter
groups = groupby(sorted_names, key=get_first_letter)

# Create a dictionary to store the counts
counts = {}

# Count the number of names for each first letter
for key, group in groups:
    counts[key] = len(list(group))

# Print the dictionary of counts to the console
print(counts)
