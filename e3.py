# Project Euler: Problem 3
# Largest Prime Factor
#
# The prime factors of 13195 are 5, 7, 13 and 29
# What is the largest prime factor of the number 600851475143 ?
#
# Answer: 6857

from Eratosthenes import primes_sieve_gen
import math

def max_prime_factor(limit):
    limRoot = math.ceil(math.sqrt(limit))
    maxPrimeFactor = 0
    
    for prime in primes_sieve_gen(limRoot):
        if (limit % prime == 0) and (prime > maxPrimeFactor):
            maxPrimeFactor = prime
            
    return maxPrimeFactor
