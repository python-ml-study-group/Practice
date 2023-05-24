#Task 1
from functools import reduce
def is_prime(n):
    if n<2:
        return False 
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
l=list(range(1,101))
prime=list(filter(is_prime,l))
print(prime)
add=reduce(lambda a,b:a+b,prime)
print(add)