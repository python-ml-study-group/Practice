from itertools import groupby
ar = {'roopesh': 'ka', 'hari': 'ap', 'nikhita': 'ap', 'sirisha': 'ap', 'mahesh': 'ts',  'srilatha':'ts'}

for item in groupby(ar, lambda x: ar[x]):
    print(item[0], list(item[1]))

