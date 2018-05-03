from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import pandas as pd
from sklearn import preprocessing
import ExcelUtility as eu

# define example
#xls="paths.xlsx"
# load dataset
#X = pd.read_excel(xls,sheetname=0)
#print(X)

# TODO: create a LabelEncoder object and fit it to each feature in X


# 1. INSTANTIATE
# encode labels with value between 0 and n_classes-1.
le = preprocessing.LabelEncoder()


# 2/3. FIT AND TRANSFORM

# TODO: create a OneHotEncoder object, and fit it to all of X

# 1. INSTANTIATE


# 2. FIT



# 3. Transform


def encodeValues(all_paths,fxnlength1,dirname):
    #convert list of list to binary form. If in Path1 function1 present then value is 1 else 0
    print("encode values")
    list=all_paths
    pathLength=len(all_paths)
    print("path length:",pathLength)
    print("fxn length:", fxnlength1)
    #created empty numpy with 0 index , added 1 value as we want to store the header labels and classes label as well
    matrix= np.zeros(shape=(pathLength, fxnlength1))

    #create labels column

    #create classes row

    #update values in numpy
    row=0
    for sublst in list:
        for item in sublst:
            pos=int(item.replace("f",""))
            pos=pos-1
            #print(sublst)
            #print(item)
            matrix[row,pos]=1
        row += 1

    nonZeroMatrix=matrix[:, np.apply_along_axis(np.count_nonzero, 0, matrix) > 0]

    printMatrixToExcel(matrix,dirname+"matrix.csv")
    printMatrixToExcel(nonZeroMatrix, dirname+"matrixWithNonZero.csv")
    return matrix

def printMatrixToExcel(matrix,fileName):
    eu.printNumpyArrayInExcel(matrix,fileName)