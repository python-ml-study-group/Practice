#Create a list containing the numbers 1 through 100. Use the filter() function to create a new list containing only the prime numbers from the original list. Use the reduce( function to calculate the sum of the prime numbers in the new list. Print the sum to the console.

from functools import reduce

#function to check if number is prime or not
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#creating a list ranging from 0-100
numbers = list(range(1, 101))

#filtering to print only prime numbers
prime_numbers = list(filter(is_prime, numbers))

#use reduce() to calculate sum of prime numbers
prime_sum = reduce(lambda x, y: x + y, prime_numbers)


print(prime_sum)
