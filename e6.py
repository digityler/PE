# Project Euler: Problem 6
# Sum square difference
#
# The sum of the squares of the first ten natural numbers is,
# 1**2 + 2**2 + ... + 10**2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)**2 = 55**2 = 3025
# Hence the difference between the sum of the squares of
# the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.
#
# Answer: 25,164,150

def difsumsqr(num):
    sumSqr = 0
    sqrSum = 0
    for n in range(1, num + 1):
        sumSqr = sumSqr + n * n
        sqrSum = sqrSum + n
    return sqrSum * sqrSum - sumSqr
