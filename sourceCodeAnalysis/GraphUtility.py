import networkx as nx
import matplotlib.pyplot as plt
import pydot
from networkx.drawing.nx_pydot import write_dot
from subprocess import check_call
import ExcelUtility as eu
import xlsxwriter

# and the following code block is not needed
# but we want to see which module is used and
# if and why it fails
def visualize_to_dot(G,path):
    # nx.draw_networkx(G)
    #plt.show()
    write_dot(G,path)

def visualize_to_png(filepath,pngfilename):
    (graph,) = pydot.graph_from_dot_file(filepath)
    #graph.draw(pngfilename)
    graph.write_png(pngfilename)
    check_call(['dot', '-Tpng', filepath, '-o', pngfilename])

def getAllPaths(G,printToExcel,dirname):
    sink_nodes = [node for node, outdegree in G.out_degree(G.nodes()).items() if outdegree == 0]
    source_nodes = [node for node, indegree in G.in_degree(G.nodes()).items() if indegree == 0]

    #for ((source, sink) for sink in sink_nodes for source in source_nodes):
     #   for path in nx.all_simple_paths(G, source=source, target=sink):
      #      print(path)
    all_paths=[]
    for i in G.edges():
        print("\n")
        for path in nx.all_simple_paths(G, source=i[0], target=i[1]):
            print(i)
            print(path)
            all_paths.append(path)
    if(printToExcel):
        workbook = xlsxwriter.Workbook('paths.xlsx')
        eu.writeToExcellists(all_paths,"paths",workbook)
    return all_paths

def getAllPathsWithoutAbbreviations(G,printToExcel,dirname):
    sink_nodes = [node for node, outdegree in G.out_degree(G.nodes()).items() if outdegree == 0]
    source_nodes = [node for node, indegree in G.in_degree(G.nodes()).items() if indegree == 0]

    #for ((source, sink) for sink in sink_nodes for source in source_nodes):
     #   for path in nx.all_simple_paths(G, source=source, target=sink):
      #      print(path)
    all_paths=[]
    for i in G.edges():
        print("\n")
        for path in nx.all_simple_paths(G, source=i[0], target=i[1]):
            print(i)
            print(path)
            all_paths.append(path)
    if(printToExcel):
        workbook = xlsxwriter.Workbook('pathsNoAbbreviation.xlsx')
        eu.writeToExcellists(all_paths,"paths",workbook)
    return all_paths

def  getAllOptimizedPaths(G,printToExcel,filename,dirname):
    all_paths=[]
    for i in G.edges():
        print("\n")
        for path in nx.all_simple_paths(G, source=i[0], target=i[1]):
            print(i)
            print(path)
            if(len(path) > 5):
             all_paths.append(path)

    if(printToExcel):
        workbook = xlsxwriter.Workbook(filename)
        eu.writeToExcellists(all_paths,"pathsoptimized",workbook)
    createPathGraphFromList(all_paths,dirname+'path.dot')
    return all_paths

def  getAllOptimizedPathsWithoutAbbreviations(G,printToExcel,filename,dirname):
    all_paths=[]
    for i in G.edges():
        print("\n")
        for path in nx.all_simple_paths(G, source=i[0], target=i[1]):
            print(i)
            print(path)
            if(len(path) > 5):
             all_paths.append(path)

    if(printToExcel):
        workbook = xlsxwriter.Workbook(filename)
        eu.writeToExcellists(all_paths,"pathsoptimized",workbook)
    createPathGraphFromList(all_paths,dirname+"pathNoAbbreviation.dot")
    return all_paths

def createPathGraphFromList(pathList,filename):
    # create dot file
    pathGraph=nx.DiGraph()
    all_paths = []
    print("List size:", len(pathList))
    for sublst in pathList:
        print("Sublist size:", len(sublst))
        for i in range(len(sublst)-1):
            pathGraph.add_edge(sublst[i],sublst[i+1])

    visualize_to_dot(pathGraph,filename)


def findPaths(G,u,n):
    if n==0:
        return [[u]]
    paths = [[u]+path for neighbor in G.neighbors(u) for path in findPaths(G,neighbor,n-1) if u not in path]
    return paths

