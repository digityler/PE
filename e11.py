# Project Euler: 11
# Largest product in a grid
#
# In the 20x20 grid below, 
# four numbers along a diagonal line have been marked in red.
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696
# What is the greatest product of four adjacent numbers in the same 
# direction (up, down, left, right, or diagonally) in the 20×20 grid?
# 
# Answer: 

import pandas as pd
import numpy as np
from fileToMatrix import *

def gridMult(file, axis):
	grid = fileToMatrix(file, True)
	dfGrid = pd.DataFrame(grid)
	maxProd = 1
	
	for line in range(20):
		beg = 0
		end = 3

		for quad in range(17):
			prodList = []
			product = 1

			if axis == 0:
				prodList = dfGrid.ix[line, beg:end]
			elif axis == 1:
				prodList = dfGrid.ix[beg:end, line]
			else:
				raise ValueError("Axis must be 0 for row or 1 for column.")

			product = np.prod(prodList)

			if product > maxProd:
				maxProd = product

			beg += 1
			end += 1

	return maxProd