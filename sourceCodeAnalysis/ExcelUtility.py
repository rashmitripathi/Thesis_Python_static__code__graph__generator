import xlsxwriter
import tempfile
import numpy as np
import os

def writeToExcel(d,sheetname,workbook):
    #dictionary_of_lists
    worksheet = workbook.add_worksheet(sheetname)
    row=0
    col=0
    for key in d.keys():
        col=0
        worksheet.write(row, col, key)
        for item in d[key]:
            print(item)
            worksheet.write(row, col + 1, item)
            col+=1
        row += 1

def writeToExcelCount(d,sheetname,workbook):
    #dict_of_integers
    worksheet = workbook.add_worksheet(sheetname)
    row=0
    col=0
    for key in d.keys():
        worksheet.write(row, col, key)
        worksheet.write(row, col + 1, d[key])
        row += 1

def writeToExcellists(list,sheetname,workbook):
    #lists of list
    worksheet = workbook.add_worksheet(sheetname)
    row=0
    col=0
    list.sort(key=len,reverse=True)
    print("List size:",len(list))
    for sublst in list:
        print("Sublist size:",len(sublst))
        col=0
        for item in sublst:
            worksheet.write(row, col, item)
            col=col+1
        row += 1

def printNumpyArrayInExcel(A,filename):
    np.savetxt(filename, A, delimiter=',', fmt='%s')