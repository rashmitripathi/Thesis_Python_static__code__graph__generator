import numpy as np
import ExcelUtility as eu

def calSimilarityIndex(path1, path2):
    # output
    unionResult = np.logical_and(path1, path2)
    unionCount = np.count_nonzero(unionResult == 1)

    xorResult = np.logical_or(path1, path2)
    xorCount = np.count_nonzero(xorResult == 1)
    #print("Output Array : ", xorCount)

    return round(unionCount / float(xorCount),1)

def getResultSimilarityMatrix(input,fileName):
    # iterate
    rows = input.shape[0]
    #print("Rows:", rows)

    result = np.zeros(shape=(rows,rows))
    for x in range(0, rows):
        for y in range(0, rows):
            #print(input[x], input[y], calSimilarityIndex(input[x], input[y]))
            result[x,y]=calSimilarityIndex(input[x], input[y])
    #print(result)
    eu.printNumpyArrayInExcel(result, fileName)
    #eu.writeToExcellists(result,sheetName,fileName)
    return result



def test():
    x = np.array([[0, 1, 1], [0, 1, 1]])
    # print(np.cov(x))

    # input
    arr1 = [1, 1, 1, 0]
    arr2 = [0, 0, 0, 1]
    arr3=  [1,0,1,1]

    arr3=np.array([arr1,arr2,arr3])
    #print(arr3)

    getResultSimilarityMatrix(arr3,"k")

test()