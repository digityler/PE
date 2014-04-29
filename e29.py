def distinctPow():
    termList = []
    for a in range(2, 101):
        for b in range(2, 101):
            termList.append(a**b)
    return len(list(set(termList)))
