# Sieve of Eratosthenes

# Returns an array of primes up to the limit specified

def primes_sieve(limit):
    limitN = limit+1
    notPrime = set()
    primes = []

    for i in range(2, limitN):
        if i in notPrime:
            continue

        for k in range(i**2, limitN, i):
            notPrime.add(k)

        primes.append(i)

    return primes

# Yields primes up to the limit specified

def primes_sieve_gen(limit):
    limitN = limit+1
    notPrime = set()

    for i in range(2, limitN):
        if i in notPrime:
            continue

        for k in range(i**2, limitN, i):
            notPrime.add(k)

        yield i
