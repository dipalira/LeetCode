def generateMatrix(n):
    
    result = [[0 for i in range(n)] for j in range(n)]
    coord = [[(i,j) for j in range(n)] for i in range(n)]
    print(coord)
    count = 1
    
    while coord:
        for x, y in coord.pop(0):
            result[x][y] = count
            count += 1
        coord = list(zip(*coord))[::-1]
        print(coord)
    print (result)
generateMatrix(3)
