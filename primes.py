"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    x = number_of_primes
    list = []
    no = 0
    i = 1
    while not(no == x):
        factors = 0
        
        i = i + 1
        for j in range(1,i):
            if(i % j == 0):
                factors = factors + 1
            if(factors == 2):
                list.append(i)
                no = no + 1
    return list
