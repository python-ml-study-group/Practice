""" Create a list containing the numbers 1 through 100. Use the ﬁlter()
function to create a new list containing only the prime numbers from the
original list. Use the reduce() function to calculate the sum of the
prime numbers in the new list. Print the sum to the console in python.
"""

from functools import reduce

# Create a list containing numbers from 1 to 100
numbers = list(range(1, 101))

# Define a function to check if a number is prime
def is_prime(n):
    flag = False
    if n < 2:
        return False
    for i in range(2, n):
        if (n % i) == 0:
            flag = True
            break
    if flag:
        return False
    else:
        return True

# Use filter() to create a new list containing only prime numbers from the original list
primes = list(filter(is_prime, numbers))

# Print the list of prime numbers to the console
print(primes)

# Use reduce() and lambda function to calculate the sum of prime numbers
sum_of_primes = reduce(lambda x, y: x + y, primes)

# Print the sum of prime numbers to the console
print(sum_of_primes)
