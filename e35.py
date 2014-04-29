#e35
#
#Find number of circular primes below one million

import math

def circularPrimes(primes):
    
    circPrimes = []
    
    for prime in primes:
        primeArray = []
        
        for i in str(prime):
            primeArray.append(i)
            
        primeLen = len(str(prime))
        rotArray[]
        j = 0
        
        while j < primeLen:

            if j == (primeLen - 1):
                rotArray[0] = primeArray[j]
            else:
                rotArray[j + 1] = primeArray[j]
            j += 1
        print(primeArray)
        print(rotArray)
        

def primes(num):

    primes = [2, 3]
    p = 5
    
    while p < num:
        i = 2
        isPrime = True
        
        while i < math.sqrt(p + 1):
            
            if p % i == 0:
                isPrime = False
                break
            i += 1
            
        if isPrime == True:
            primes.append(p)
        p += 2
        
    return primes
