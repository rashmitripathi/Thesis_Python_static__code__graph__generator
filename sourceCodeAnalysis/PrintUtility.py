from anytree import RenderTree
from anytree.exporter import DotExporter
from anytree.dotexport import RenderTreeGraph
from subprocess import check_call

import os

#  graphviz needs to be installed for the next line!

def printTree(treeNode):
    print('Current working directory path:', os.getcwd())
    for pre, fill, node in RenderTree(treeNode):
        print("%s%s" % (pre, node.name))
    DotExporter(treeNode).to_dotfile("tree.dot")
    #check_call(['dot', '-Tpng', 'tree.dot', '-o', 'OutputFile.png'])
    #RenderTreeGraph(treeNode).to_picture("tree.png")
    #DotExporter(treeNode).to_picture("a.jpg")