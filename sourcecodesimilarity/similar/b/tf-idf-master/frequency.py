import math
#this calculates the frequencies for the tf-idf

def termFreq(nTerms, totalTerms):
    #returns the number of times the term appears in the document by the total number of terms
    return nTerms / totalTerms

def inversedf(totalDoc, nDocWTerm):
    #returns natural log of the total number of documents divided by the number of documents with the term
    return math.log(totalDoc / nDocWTerm)