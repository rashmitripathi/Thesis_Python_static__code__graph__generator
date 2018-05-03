import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import openpyxl

#word_tokenize accepts a string as an input, not a file.
stop_words = set(stopwords.words('english'))
# common in built functions in python :https://docs.python.org/3/library/functions.html
numbers_set=set(['0','1','2','3','4','5','6','7','8','9','10','1.','2.','3.','4.','5.','6.','7.','8.','9.','10.','#','(e.g.','True)','len','int','dict','0:len','next','min','float','set','iter','bool','type','sqrt','instance','abs','dict','help','min','setattr','all','dir','hex','next','slice','any','divmod','id','object','sorted','ascii','enumerate','input','oct','staticmethod','bin','eval','int','open','str','bool','exec','isinstance','ord','sum','bytearray','filter','issubclass','pow','super','bytes','float','iter','print','tuple','callable','format','len','property','type','chr','frozenset','list','range','vars','classmethod','getattr','locals','repr','zip','compile','globals','map','reversed','__import__','complex','hasattr','max','round','delattr','hash','memoryview','set','fn','test'])

stop_words=stop_words.union(numbers_set)
print("stop words:",stop_words)

def isStopWord(str):
  print(str)
  if str in stop_words:
    print("True")
    return True
  return False


def removeStopwords(fileName):
 x=0
 col = "A"
 row = x

 # Function : to remove the stopwords from the excel file
 xfile = openpyxl.load_workbook(fileName)
 xl = xfile['classInfo']

 for row in xl.iter_rows(min_row=1, min_col=2, max_row=1000, max_col=1000):
     for cell in row:
         if(cell.value is not None):
          print(cell.value, end=" ")
          if (isStopWord(cell.value.strip())):
             cell.value = ""

 xfile.save('dataafterstopwordsremoval.xlsx')



#removeStopwords('dataold.xlsx')
