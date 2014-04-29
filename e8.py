def seriesProduct():
    seriesArray = []
    productMax = 0
    product = 1
    
    inFile = open("C:\Python33\Code\e8data.txt", "r")
    
    for line in inFile:
        seriesArray.append(line)
    for i in 
        for j in range(6):
            product *= seriesArray[j]
        if product > productMax:
            productMax = product
        product = 1
    print(productMax)
