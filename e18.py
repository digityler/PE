# Project Euler: 18 and 67
#
# By starting at the top of the triangle below and moving to adjacent
# numbers on the row below, the maximum total from top to bottom is 23.
#          3
#         7 4
#        2 4 6
#       8 5 9 3
# That is, 3 + 7 + 4 + 9 = 23
# Find the maximum total from top to bottom in triangle.txt
# a 15K text file containing a triangle with one-hundred rows.
#
# 18 Answer: 1074
# 67 Answer: 7273

def triSum(file):	
	triangle = []
	data = open(file, 'r')

	for line in data:
		triangle.append([int(num) for num in line.strip().split()])

	row = len(triangle) - 2

	while row >= 0:
		rowLen = len(triangle[row])

		for col in range(rowLen):
			triangle[row][col] = triangle[row][col] + max(triangle[row + 1][col], triangle[row + 1][col + 1])

		row -= 1

	return triangle[0][0]
