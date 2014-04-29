# Project Euler: Problem 7
# 10001st prime
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13
# we can see that the 6th prime is 13
# What is the 10001st prime number?
#
# Answer: 104,743

from Eratosthenes import primes_sieve_gen
import math

def nth_prime(num):
    sieveLimit = math.ceil(num * math.log(num)) * 2
    prime = primes_sieve_gen(sieveLimit)
    for i in range(num):
        nthPrime = next(prime)
    return nthPrime
