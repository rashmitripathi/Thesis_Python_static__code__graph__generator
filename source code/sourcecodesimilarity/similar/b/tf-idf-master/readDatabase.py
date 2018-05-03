#this reads the database file that contains the idf calculations
import frequency as freq
from bs4 import BeautifulSoup
import requests

#change this url to web scrape a different website - note that some websites will block requests to scrape their website as part of their EULA
url = "http://m.mlb.com/news/article/226145774/nationals-win-their-seventh-consecutive-game/?topicId=27118122"

def readFile(fileName):
    #this function reads the database file into a map for the idf part
    f = open(fileName, 'r')
    s = f.read()
    lineList = s.split("\n")  #list of all the lines from the txt file

    idfMap = {}

    for i in range(len(lineList)-1):
        stringLine = lineList[i]  #stores a string of one line from the file
        wordValueList = stringLine.split(":")  #stores a list with the 1st element as the word, and the 2nd element as the idf value
        idfMap[wordValueList[0]] = wordValueList[1]


    f.close()
    return idfMap

def readIn(articleString):
    s = articleString
    s = s.replace('\n', ' ')
    s = s.replace('\r', ' ')
    s = s.replace('\t', ' ')

    wordlist = s.split(' ')
    keywordlist = {}  #contains the map of all the words mapped to the number of times they appear
    numOfWords = 0  #number of words counter
    for i in range(len(wordlist)):
        word = wordlist[i]
        if word.__contains__(','):
            word = word.replace(',', '')
        if word.__contains__('.'):
            word = word.replace('.', '')
        if word.__contains__('?'):
            word = word.replace('?', '')
        if word.__contains__('!'):
            word = word.replace('!', '')
        if word.__contains__('"'):
            word = word.replace('"', '')
        if word.__contains__('('):
            word = word.replace('(', '')
        if word.__contains__(')'):
            word = word.replace(')', '')
        if word.__contains__('['):
            word = word.replace('[', '')
        if word.__contains__(']'):
            word = word.replace(']', '')
        if word.__contains__('{'):
            word = word.replace('{', '')
        if word.__contains__('}'):
            word = word.replace('}', '')
        if word.__contains__(':'):
            word = word.replace(':', '')
        if word.__contains__(';'):
            word = word.replace(';', '')
        if word.__contains__('”'):
            word = word.replace('”', '')
        if word.__contains__('“'):
            word = word.replace('“', '')
        if word.__contains__('<'):
            word = word.replace('<', '')
        if word.__contains__('>'):
            word = word.replace('>', '')
        if word.__contains__('|'):
            word = word.replace('|', '')
        if word.__contains__('='):
            word = word.replace('=', '')
        if word.__contains__('+'):
            word = word.replace('+', '')
        if word.__contains__('\\'):
            word = word.replace('\\', '')
        if word.__contains__('/'):
            word = word.replace('/', '')








        word = word.lower()

        if len(keywordlist) == 0:
            keywordlist[word] = 1
        else:
            if keywordlist.__contains__(word):
                keywordlist[word] +=1
            else:
                keywordlist[word] = 1
        numOfWords = i+1


    #returns a list containing
    #index 0: a map of all the words in the document that is mapped to the number of times they appear,
    #index 1: and the total number of words in the document
    return [keywordlist, numOfWords]


#main program
finalCalc = {}  #map that holds all of

databaseIDFMap = readFile("database.txt")

#web scraping part
data = requests.get(url).text
soup = BeautifulSoup(data, "html.parser")
for elem in soup.find_all(['script', 'style', 'head', 'title']):
    elem.extract()
texts = soup.get_text()

print(texts)
filelist = readIn(texts)

"""
#for files
file = open("textfile.txt", 'r')
filestr = file.read()
filelist = readIn(filestr)
file.close()
"""

#removes '' blanks from the dictionary
try:
    filelist[1] -= filelist[0]['']
    del filelist[0]['']
except KeyError:
    print("Does not exist")

numOfWords = filelist[1]
print(filelist)


#calculates the tf-idf and adds it to the dictionary finalCalc
for i in filelist[0].keys():
    #print(i)
    try:
        finalCalc[i] = freq.termFreq(filelist[0][i], numOfWords) * float(databaseIDFMap[i])
    except KeyError:
        finalCalc[i] = -1



#prints all the dictionary keys and values to the output.txt file
outputFile = open("output.txt", 'w')

finalCalcOpp = {}

for term in finalCalc.keys():
    finalCalcOpp[finalCalc[term]] = term

for value in sorted(finalCalc.values()):
    finalString = "" + str(finalCalcOpp[value]) + ":" + str(value) + "\n"
    print(finalString)
    outputFile.write(finalString)

outputFile.close()
