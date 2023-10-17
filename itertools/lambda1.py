def dosomething(lst, func):
    for i in lst:
        print(func(i))

l = [1, 2, 3, 4, 5]
print("Square of each element in the list: ")
dosomething(l, lambda num: num * num)

print("Cube of each element in the list: ")
dosomething(l, lambda num: num * num * num)

def add(a, b):
    return a + b

add = lambda a, b: a + b
