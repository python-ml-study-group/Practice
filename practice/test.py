


import math
i = 2
count = 0
while count < 5:
    _sqrt = math.sqrt(i)
    if _sqrt == int(_sqrt):
        print("The perfect square: ", i)
        count += 1
    i += 1

