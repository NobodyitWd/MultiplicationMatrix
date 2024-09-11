import ast

a = []

def Plus(matrixA,matrixB):
    if type(matrixA) == list and type(matrixB) == list and len(matrixA) == len(matrixB) and len(matrixA[0]) == len(matrixB[0]):
        for x in range(len(matrixB)):
            for y in range(len(matrixB[0])):
                matrixA[x][y] += matrixB[x][y]
        return matrixA
    else:
        print("You can add only MATRIX and size matrixA == size matrixB!")

def Minus(matrixA,matrixB):
    if type(matrixA) == list and type(matrixB) == list and len(matrixA) == len(matrixB) and len(matrixA[0]) == len(matrixB[0]):
        for x in range(len(matrixB)):
            for y in range(len(matrixB[0])):
                matrixA[x][y] -= matrixB[x][y]
        return matrixA
    else:
        print("You can subtract only MATRIX and size matrixA == size matrixB!")

def Multiplication(matrixA,matrixB):
    if type(matrixA) == int and type(matrixB) == list:
        for x in range(len(matrixB)):
            for y in range(len(matrixB[0])):
                matrixB[x][y] *= matrixA
        return matrixB
    if type(matrixA) == list and type(matrixB) == int:
        for x in range(len(matrixA)):
            for y in range(len(matrixA[0])):
                matrixA[x][y] *= matrixB
        return matrixA
    if type(matrixA) == int and type(matrixB) == int and (matrixA[0]) == len(matrixB):
        newM = []
        for h in range(len(matrixA)):
            timeM = [0 for o in range(len(matrixB[0]))]
            for x in range(len(matrixB[0])):
                for y in range(len(matrixB)):
                    timeM[x] += matrixB[y][x]*matrixA[h][y]
            newM.append(timeM)
        return newM
    else:
        print("matrixA[j] != matrixB[i]")

def Determinant(matrix):
    global a
    list1 = []
    newMatrix = []
    timeM = []
    q = "["
    for h in range(len(matrix)-1):
        newMatrix.append([0]*(len(matrix)-1))
    if len(matrix[0]) == len(matrix):
        for z in range(len(matrix)):
            for x in range(len(matrix)):
                for y in range(len(matrix)):
                    if x != 0 and y != z:
                        timeM.append(matrix[x][y])
                    if len(a) != len(matrix[0]):
                        a.append(matrix[0][y])
    else:
        print("matrixA[j] != matrixB[i]")
    l = 0
    k = 1
    for z in range(len(matrix[0])):
        for x in range(len(newMatrix)):
            for y in range(len(newMatrix)):
                if l != len(timeM):
                    if len(timeM) == 12:
                        newMatrix[x][y] += timeM[l]
                    else:
                        newMatrix[x][y] = timeM[l]
                    l += 1
        if len(newMatrix) == 2:
            list1.append(((-1)**k)*(newMatrix[0][0]*newMatrix[1][1]-newMatrix[0][1]*newMatrix[1][0]))
            k+=1
            newMatrix = []
            for h in range(len(matrix) - 1):
                newMatrix.append([0] * (len(matrix) - 1))
        else:
            q += str(newMatrix) + ","

    if len(q) != 1:
        q = q[:-1] + "]"
        q = ast.literal_eval(q)
        return q
    else:
        finaly = sum(list1)
        return finaly

matrixB = [[1,2,3], [4,5,6],[7,8,9]]
matrixA = [[1,2,5], [3,4,4], [5,6,9]]
#matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,-12],[13,14,15,16]]
matrix = [[2,-5,1,2],[-3,7,-1,4],[5,-9,2,7],[4,-6,1,2]]
"""for i in multiplication(matrixA,matrixB):
    print(i)"""
nw = []

for i in range(len(Determinant(matrix))):
    nw.append(Multiplication(a[i]*((-1)**(i+1)),Determinant(matrix)[i]))
    print(nw[i],a[i])
