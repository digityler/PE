# Project Euler: Problem 4
# Largest Palindrome Product
#
# A palindromic number reads the same both ways. The largest palindrome made from
# the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# Answer: 906,609

def palinum():
    a = 999
    b = 999
    palins = []
    prod = 0
    while a > 99 or b > 99:
        prod = a * b
        prod = str(prod)
        if prod[:1] == prod[5:] and prod[1:2] == prod[4:5] and prod[2:3] == prod[3:4]:
            palins.append(int(prod))
            b -= 1
        elif b > 99:
            b -= 1
        else:
            a -= 1
            b = 999
    return max(palins)
