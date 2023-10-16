import math

def is_perfect_square(i):
    _sqrt = math.sqrt(i)
    if _sqrt == int(_sqrt):
        return True
    else:
        return False

i = 2
count = 0
while count < 5:
    if is_perfect_square(i):
        print("The perfect square: ", i)
        count += 1
    i += 1


def is_apple (_object):
    if _object.color == 'red':
        return True
def is_orange(_object):
    if _object.color == 'orange':
        return True