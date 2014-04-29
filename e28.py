def spiralDiagonal(num):
    spiralSum = 1
    i = 1
    for step in range(2, num + 1, 2):
        for j in range(1, 5):
            i += step
            spiralSum += i
    return spiralSum
