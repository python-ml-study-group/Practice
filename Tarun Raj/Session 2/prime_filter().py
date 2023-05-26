from functools import reduce

# Create a list containing numbers from 1 to 100
numbers = list(range(1, 101))

# Define a function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Use filter() to create a new list containing only prime numbers from the original list
primes = list(filter(is_prime, numbers))

# Print the list of prime numbers to the console
print(primes)

# Use reduce() and lambda function to calculate the sum of prime numbers
sum_of_primes = reduce(lambda x, y: x + y, primes)

# Print the sum of prime numbers to the console
print(sum_of_primes)
