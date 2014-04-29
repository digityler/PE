# Project Euler: 15
# Lattice paths
#
# Starting in the top left corner of a 2x2 grid, and only being able to move
# to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20x20 grid?
#
# Answer: 137,846,528,820


from scipy.misc import comb

def latticePath(gridSize):
    pathSum = 0
    for k in range(gridSize + 1):
        pathSum += comb(gridSize, k, 1)**2
    return pathSum
