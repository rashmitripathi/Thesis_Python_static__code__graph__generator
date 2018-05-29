import os
import threading
import frequency as freq
#this is a program written by Nathaniel Young for tf-idf

class myThread(threading.Thread):
    def __init__(self, folderlist, begin, end):
        threading.Thread.__init__(self)
        self.folderlist = folderlist
        self.begin = begin
        self.end = end

    def run(self):
        iterateAndCreate(self.folderlist, self.begin, self.end)



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

def splitFile(filename):
    f = open(filename, 'r')
    s = f.read()
    index = 0
    f.close()

    #separates the articles in each text file, and calls the readIn function
    while s.find("<doc", index) >= index:
        a = s.find("\">", index)
        b = s.find("</doc>", index)

        articleString = s[a+2:b]
        #print(articleString)
        total.append(readIn(articleString))

        index = b+1


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

def iterateAndCreate(folderlist, begin, end):
    for i in range(begin, end):

        if not folderlist[i].startswith('.'):
            filelist = os.listdir(filepath + folderlist[i])  # holds the list of files in each folder
            print("This is the list of files in folder: " + folderlist[i])
            print(filelist)
            print("")

            for j in range(len(filelist)):

                if not filelist[j].startswith('.'):
                    splitFile(filepath + folderlist[i] + "/" + filelist[j])
                    # total.append(readIn(testpath + folderlist[i] + "/" + filelist[j]))




#main program - it reads in all of the files, and then

filepath = "../../../Documents/wikipedia/"
#testpath = "testFiles/"

folderlist = os.listdir(filepath)  #holds the list of folders
total = []  #a list of lists of [a map of the number of times a word appears in a document, the number of words in the document]

print("This is the list of folders")
print(folderlist)
print("")

thread1 = myThread(folderlist, 0, 15)
thread2 = myThread(folderlist, 15, 30)
thread3 = myThread(folderlist, 30, 45)
thread4 = myThread(folderlist, 45, 60)
thread5 = myThread(folderlist, 60, 75)
thread6 = myThread(folderlist, 75, 90)
thread7 = myThread(folderlist, 90, 105)
thread8 = myThread(folderlist, 105, 120)
thread9 = myThread(folderlist, 120, 135)

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread9.start()


thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
thread6.join()
thread7.join()
thread8.join()
thread9.join()






numOfDoc = len(total)  #the number of documents
docNumWithWord = calcTotalTimes(total)


#print(len(total))
#print(total)
#print(docNumWithWord)


idfMap = {}  #map of the idf calculations, [key, idf value]
for j in docNumWithWord.keys():
    tempIDF = freq.inversedf(numOfDoc, docNumWithWord[j])
    idfMap[j] = tempIDF

try:
    del idfMap['']
except KeyError:
    print("Does not exist")

print(idfMap)

#writes the idf map to the database file
databaseFile = open("database.txt", 'w')
for term in idfMap.keys():
    finalString = "" + term + ":" + str(idfMap[term]) + "\n"
    databaseFile.write(finalString)

databaseFile.close()

