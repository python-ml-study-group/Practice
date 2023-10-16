
from itertools import permutations, combinations, product

ar = ['Leo', 'Bhagavant Kesari', 'Tiger Nageshwr', 'Ghost', 'Ganapat']
counter = 0
print ("The permutations are: ")
for p in permutations(ar):
    print(p)

ar = ['Leo', 'Bhagavant Kesari', 'Tiger Nageshwr', 'Ghost', 'Ganapat']
print ("The combinations are: ")
for c in combinations(ar, 5):
    print(c)
