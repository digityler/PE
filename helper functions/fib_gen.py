def fibGen(maxNum):
    fib1 = 0
    fib2 = 1
    nextFib = 1
    while nextFib <= maxNum:
        yield nextFib
        nextFib = fib1 + fib2
        fib1 = fib2
        fib2 = nextFib
