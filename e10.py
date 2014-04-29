# Project Euler: Problem 10
# Summation of primes
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
# Find the sum of all primes below two million.
#
# Answer: 142,913,828,922

from Eratosthenes import primes_sieve_gen

def sum_primes(limit):
    pSum = 0
    for prime in primes_sieve_gen(limit):
        pSum += prime
    return pSum
