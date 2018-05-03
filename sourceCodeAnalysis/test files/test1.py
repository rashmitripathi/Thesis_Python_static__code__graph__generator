from anytree import Node, RenderTree
import os

import ExcelUtility
import xlsxwriter
import PrintUtility
import re
import stopWordsRemoval
import networkx as nx
import StringUtility as su
import GraphUtility as gu
import TimeUtility
import AbbreviatedNamesUtility as an
import CustomEncodingUtility as ceu
"""
    This function will generate the file names in a directory  tree by walking the tree either top-down or bottom-up. 
    For each directory in the tree rooted at directory top (including top itself), it yields a 3-tuple (dirpath, dirnames, filenames).
"""
def get_filepaths(directory):
    start = TimeUtility.start()
    anu=an.Abbreviations()
    rootNode = Node("tensorflow")
    file_paths = []                                                        # List which will store all of the full filepaths.
    fileFxnDictionary = {}
    fileImportDictionary = {}
    fileClassDictionary = {}
    callerFxnArgumentsDictionary={}
    callerCalleeFxn={}
    calleFxnArguments={}
    fileFxnCount={}
    fileImportCount={}
    fileClassCount={}
    uniqueImports=[]
    callerCalleePath=[]
    fxnGraph = nx.DiGraph()

    fxnList=[]
    classList=[]
    importList=[]

    for root, directories, files in os.walk(directory):                    # Walk the tree.


        for filename in files:
            str=filename.__str__()

            #print("root",root)
            filepath=root.replace("\\","/")                               # Join the two strings in order to form the full filepath.
            filepath=filepath+"/"+filename
            #filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.
            #module = importlib.import_module(filepath)
            #my_class = getattr(module, 'MyClass')
            #my_instance = my_class()
            #dir()
#           #print("filepath : ",filepath," members are :",dir(module(filepath)))
            #print("filepath : ", filepath)
            if(not filepath.endswith(".py")):
                continue
            localFileNode = Node(filepath.replace(directory,""), parent=rootNode)
            file = open(filepath, "r+",encoding="utf8")
            variable=[]
            functionName=[]
            className=[]
            importModules=[]
            isNextWordfxn=False
            isNextWordclass=False
            isNextWordImport=False
            isNewWord=False
            classChildren=False
            fxnChildren=False
            mainFxnNode=None
            clsNode=None

            for word in file.read().split():
                if(stopWordsRemoval.isStopWord(word) or word.__len__()<=2):
                    continue
                if(isNextWordclass):
                 if(word.__contains__("(")) :
                   className.append(word)
                   classChildren=True
                   clsNode = Node("class:" + word, parent=localFileNode)
                 isNextWordclass=False
                 #print(word)
                elif(isNextWordfxn):
                 print("fxnname",word)
                 if("(" in word):
                     arg=word.split("(")[1]
                     word=word.split("(")[0]

                 functionName.append(word.lower())
                 isNextWordfxn=False

                 if(classChildren and (not fxnChildren)):
                  mainFxnNode = Node("Fxn:" + word, parent=clsNode)
                 elif(fxnChildren):
                  fxnNode = Node("Fxn:" + word, parent=mainFxnNode)
                  callerCalleeFxn.update({mainFxnNode.name,fxnChildren})
                 else:
                  fxnNode = Node("Fxn:" + word, parent=localFileNode)
                 fxnChildren = True
                 #print(word)
                elif(isNextWordImport):
                 importModules.append(word)
                 isNextWordImport=False
                 importNode = Node("Import:" + word, parent=localFileNode)
                 #print(word)

                if (word == "def"):
                    isNextWordfxn = True
                    isNewWord=True
                    fxnChildren = False
                    #print("true")
                elif (word == "class"):
                    isNextWordclass = True
                    isNewWord=True
                    fxnChildren=False
                elif (word == "import"):
                    isNextWordImport = True
                    isNewWord=True
                elif (checkWordForValidFunction(word) and fxnChildren):
                    print("got new function lets see::::",word)
                    if(fxnChildren and mainFxnNode is not None):
                        fxnNode = Node("Fxn:" + word, parent=mainFxnNode)
                        callerCalleeFxn[mainFxnNode.name]=[word]
                        fxnGraph.add_edge(anu.get(su.sanitize(mainFxnNode.name)),anu.get(su.sanitize(word)))


           # print("File:",filepath,"Functions:",functionName)
            #print("File:",filepath,"Classes:", className)
            #print("File:",filepath,"Import:", importModules)
            if(len(functionName) != 0):
                fileFxnDictionary.update({filepath.replace(directory,""):set(functionName)})
                fileFxnCount[filepath.replace(directory,"")]=len(set(functionName))
            if (len(className) != 0):
                fileClassDictionary.update({filepath.replace(directory,""): set(className)})
                fileClassCount[filepath.replace(directory, "")]=len(set(className))
            if (len(importModules) != 0):
                fileImportDictionary.update({filepath.replace(directory,""): set(importModules)})
                fileImportCount[filepath.replace(directory, "")]= len(set(importModules))
                uniqueImports.append(importModules)

    #print(len(fileFxnDictionary.values()))
    workbook = xlsxwriter.Workbook('data.xlsx')
    workbook1 = xlsxwriter.Workbook('function.xlsx')
    workbook2=xlsxwriter.Workbook('count.xlsx')

    ExcelUtility.writeToExcel(callerCalleeFxn, "CallerCalleFxn", workbook1)
    ExcelUtility.writeToExcel(anu.shortNames, "FxnAbbre.", workbook1)
    ExcelUtility.writeToExcel(fileFxnDictionary,"functionInfo",workbook)
    ExcelUtility.writeToExcel(fileClassDictionary, "classInfo",workbook)
    ExcelUtility.writeToExcel(fileImportDictionary, "importInfo",workbook)
    ExcelUtility.writeToExcelCount(fileFxnCount, "fxncount", workbook2)
    ExcelUtility.writeToExcelCount(fileImportCount, "importcount", workbook2)
    ExcelUtility.writeToExcelCount(fileClassCount, "classcount", workbook2)
    dumpclean(callerCalleeFxn)

    print("Unique Imports are:",len(uniqueImports))
    gu.visualize_to_dot(fxnGraph,"fxn.dot")
    gu.getAllPaths(fxnGraph,True)
    #visualize tha paths and get all the optimized paths of nodes that is this
    # function is calling this functioon and further on.. path1: f1 f2 f3 f4 f5 f6 f7
    # the results will be saved in excel file as
    filename='pathsoptimized.xlsx'
    all_paths=gu.getAllOptimizedPaths(fxnGraph, True,filename)
    print("anu.counter:",anu.counter)
    callerMatrix=ceu.encodeValues(all_paths,anu.counter)
    TimeUtility.end(start)
    #caller=callerMatrix()

    #caller.cleanInput(callerCalleeFxn)
    #stopWordsRemoval.removeStopwords('dataold.xlsx')
    #DeterMinePaths.determine(callerCalleeFxn)

    PrintUtility.printTree(rootNode)

def dumpclean(obj):
    if type(obj) == dict:
        for k, v in obj.items():
            if hasattr(v, '__iter__'):
                print(k)
                dumpclean(v)
            else:
                print('%s : %s' % (k, v))
    elif type(obj) == list:
        for v in obj:
            if hasattr(v, '__iter__'):
                dumpclean(v)
            else:
                print(v)
    else:
        print(obj)

def checkWordForValidFunction(word):

    if(word.__contains__("(")):
       print("Check for function children:", word)
       word = word.split("(")[0]
       word = re.sub("\d|\)|\(+", "", word)
       print("word after formatting:",word)
       if(not word.__len__() == 0):
        #print("yes yes yes")
        return True

    return False



#full_file_paths = get_filepaths("E:/Thesis/sourceCodeAnalysis/source code/tensorflow")

full_file_paths = get_filepaths("E:/Thesis/source code/keras")
#print(dir("E:/DR/tensorflow/python/ops/math_ops.py"))
#print(dir(a))
#print(dir("C:/Users/Puchu/PycharmProjects/MyFirstPythonProject/part3/AmericanFlag.py"))
#print(full_file_paths)