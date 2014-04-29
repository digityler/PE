def fileToMatrix(file, toInt=False):
    mtrx = []

    for line in open(file, 'r'):
        line = line.strip().split()
    
        if toInt == True:
            line = list(map(int, line))
      
        mtrx.append(line)
  
    return mtrx