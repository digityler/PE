# Project Euler: Problem 5
# Smallest Multiple
#
# 2520 is the smallest number that can be divided
# by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is
# evenly divisible by all of the numbers from 1 to 20?
#
# Answer: 232,792,560

def smallmult():
    smlMult = 1000000
    isDiv = False
    while isDiv == False:
        for i in range(11, 21):
            if smlMult % i != 0:
                isDiv = False
                smlMult += 20
                break
            isDiv = True
    return smlMult
