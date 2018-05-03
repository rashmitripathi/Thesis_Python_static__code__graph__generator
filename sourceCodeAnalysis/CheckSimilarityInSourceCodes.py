import construct_static_graph as csg
from anytree import Node, RenderTree,AsciiStyle, PreOrderIter,findall,Walker
import Matrices as ma

def check(dirnamea,dirnameb,filepath1,filepath2):
    tree1,list1=csg.analyze(dirnamea,filepath1)
    tree2,list2=csg.analyze(dirnameb,filepath2)

    totalCount=0
    similarCount=0
    intersectionCount=0

    for x in PreOrderIter(tree1):
            size=len(findall(tree2, filter_=lambda node: node.name in (x.name)))
            similarCount=similarCount+size
            if(size == 0):
                intersectionCount=intersectionCount+1
    for x in PreOrderIter(tree2):
            size=len(findall(tree1, filter_=lambda node: node.name in (x.name)))
            if(size == 0):
                intersectionCount=intersectionCount+1
    print("similar:",similarCount)
    print("intersectioncount:", intersectionCount)
    print("by nodes:",calculateJaccardSimilarity(similarCount,intersectionCount))

    #check for matrices
    ma.compare(list1,list2)






def calculateJaccardSimilarity(similar,intersection):
    return round(similar / float(intersection), 1)

a="E:/Thesis/source code/sourcecodesimilarity/nonsimilar/a"
b="E:/Thesis/source code/sourcecodesimilarity/nonsimilar/b"

c="E:/Thesis/source code/sourcecodesimilarity/similar/a"
d="E:/Thesis/source code/sourcecodesimilarity/similar/b"
check("a","b",a,b)
check("c","d",c,d)