""" Create a list containing the numbers 1 through 100. Use the ﬁlter()
function to create a new list containing only the prime numbers from the
original list. Use the reduce() function to calculate the sum of the
prime numbers in the new list. Print the sum to the console in python.
"""

from functools import reduce
ListofNumbers = list(range(1, 101))
print(ListofNumbers)     # Creates the list with numbers 1 to 100 
def is_prime(n):         # Function to find the prime number
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
primenumbers = list(filter(is_prime, ListofNumbers)) # Filters the numbers from range of numbers that satisfies the defined function is_prime
print(primenumbers)
sum_of_primenumbers = reduce(lambda x, y: x + y, primenumbers) # calculates the sum of prime numbers from the list primenumbers and assigns that sum as s single value to sum_of_primenumbers
print(sum_of_primenumbers) 