# Project Euler: Problem 16
# Power digit sum
#
# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2**1000?
#
# Answer: 1366

def powDigSum(num):
    s = 0
    expNum = str(2**num)
    for c in expNum:
        s += int(c)
    print(s)
