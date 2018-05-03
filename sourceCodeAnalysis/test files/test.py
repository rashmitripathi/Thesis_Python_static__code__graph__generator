
#import inspect

#print(inspect.getmodulename("E:/Thesis/sourceCodeAnalysis/source code/tensorflow/python/util/compat.py"))

#print(inspect.isfunction(testIsSequence()))

import numpy as np


#from pylint.lint import Run
#import a
#filename="E:/Thesis/sourceCodeAnalysis/source code/tensorflow/python/lib/io/file_io.py"
#Run(filename)
#Run(['--errors-only', filename])


import inspect

def callee():
    return inspect.getouterframes(inspect.currentframe())[1][1:4]

def caller():
    return inspect.getouterframes(inspect.currentframe())[2][1:4]

labels=np.arange('path1','path30')

print(labels)