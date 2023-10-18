from itertools import cycle
from collections import deque
names = ['raymond', 'rachel', 'matthew', 'roopesh', 'nikhita', 'shireesha', 'hari', 'sirisha', 'mahesh', 'srilatha']
names = deque (names)
groups = ['team a', 'team b']
for group in cycle(groups):
    print(group, names.popleft())
    if len(names) == 0:
        break


