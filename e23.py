# Project Euler: 23
# Non-abundant sums
#
# A perfect number is a number for which the sum of its proper divisors is exactly
# equal to the number. For example, the sum of the proper divisors of 28 would
# be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than
# n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number
# that can be written as the sum of two abundant numbers is 24. By mathematical
# analysis, it can be shown that all integers greater than 28123 can be written as
# the sum of two abundant numbers. However, this upper limit cannot be reduced any
# further by analysis even though it is known that the greatest number that cannot
# be expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of
# two abundant numbers.
#
# Answer: 4,179,871

from itertools import combinations

def abundantSum():
    AbundantLimit = 28124
    abundant = []
    nonAbundant = set()
    
    {nonAbundant.add(num) for num in range(1, AbundantLimit)}
    
    for j in range(1, AbundantLimit):
        divSum = 0
        divisors = []
        
        for k in range(1, j):
            
            if j % k == 0:
                divisors.append(k)
                
        divSum = sum(divisors)
        
        if divSum > j:
            abundant.append(j)
            
    abSum = {sum(pair) for pair in combinations(abundant, 2)}
    {abSum.add(selfSum*2) for selfSum in abundant}
    nonAbundant = nonAbundant.difference(abSum)
    
    return sum(list(nonAbundant))
