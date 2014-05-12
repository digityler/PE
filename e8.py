# Project Euler: 8
# Largest product in a series
#
# Find the greatest product of five consecutive digits in the 1000-digit number.
# See data\e8_data.txt file
#
# Answer: 40,824

def seriesProduct():
    seriesArray = []
    productMax = 0
    product = 1
    
    inFile = open("data\e8_data.txt", "r")
    
    for line in inFile:
        seriesArray.append(line)
    for i in 
        for j in range(6):
            product *= seriesArray[j]
        if product > productMax:
            productMax = product
        product = 1
    print(productMax)
