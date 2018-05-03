import os
import frequency as freq
#this is a program written by Nathaniel Young for tf-idf

def readIn(fileName):
    f = open(fileName, 'r')  #f is the file object
    s = f.read()  #s means string from the whole file
    s = s.replace('\n', ' ')
    s = s.replace('\r', ' ')
    s = s.replace('\t', ' ')
    f.close()
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

def calcTotalTimes(total):
    totalAppearance = {}  #holds the map of the number of documents that contain that word
    for i in range(len(total)):
        tempMap = total[i][0]

        for word in tempMap.keys():  #iterates through all the keys in each list
            if totalAppearance.__contains__(word):
                totalAppearance[word] += 1
            else:
                totalAppearance[word] = 1

    return totalAppearance



#main program - it reads in all of the files, and then

filelist = os.listdir("englishPaper")
total = []  #a list of lists of [a map of the number of times a word appears in a document, the number of words in the document]

for i in range(len(filelist)):
     total.append(readIn("englishPaper/" + filelist[i]))

numOfDoc = len(total)  #the number of documents
docNumWithWord = calcTotalTimes(total)

print("Number of documents: " + str(len(total)))
print("total")
print(total)
print("map the number of documents that contain a word")
print(docNumWithWord)

idfMap = {}  #map of the idf calculations
for j in docNumWithWord.keys():
    tempIDF = freq.inversedf(numOfDoc, docNumWithWord[j])
    idfMap[j] = tempIDF

print("idf map")
print(idfMap)

#writes the idf map to the database file
databaseFile = open("database.txt", 'w')
for term in idfMap.keys():
    finalString = "" + term + ":" + str(idfMap[term]) + "\n"
    databaseFile.write(finalString)

databaseFile.close()
