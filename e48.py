# Project Euler: Problem 48
# Self powers
#
# The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317
# Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000
#
# Answer: 9,110,846,700

def power_series():
    powSum = 0
    for i in range(1, 1001):
        powSum += i**i
    return powSum % 10**10
