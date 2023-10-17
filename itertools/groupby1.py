from itertools import groupby
ar = {'roopesh': 'ka', 'hari': 'ap', 'nikhita': 'ap', 'sirisha': 'ap', 'mahesh': 'ts',  'srilatha':'ts'}

# Based on the first name, group these names
# Output: [('r', ['roopesh']), ('h', ['hari']), ('n', ['nikhita']), ('m', ['mahesh']), ('s', ['sirisha', 'srilatha'])]
for item in groupby(ar, lambda x: ar[x]):
    print(item[0], list(item[1]))

