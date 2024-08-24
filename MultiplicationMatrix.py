def multiplication(matrixA,matrixB,width,finely=""):
    try:
        newM = []
        for h in range(len(matrixA)):
            timeM = [0 for o in range(width)]
            for x in range(width):
                for y in range(width):
                    timeM[x] += matrixB[x][y]*matrixA[h][y]
                    print(timeM,matrixB[x][y],matrixA[h][y],x,y,h)
            newM.append(timeM)
        return newM
    except:
        print("матрица(А) больше чем матрица(Б)")


matrixA = [[49, 55, 37,22], [50, 52, 57,23], [53, 41, 47,6]]
matrixB = [[40, 37, 44,6], [44, 47, 55,4], [47, 50, 44,2], [36, 36, 36,3]]
print(multiplication(matrixA,matrixB,4))