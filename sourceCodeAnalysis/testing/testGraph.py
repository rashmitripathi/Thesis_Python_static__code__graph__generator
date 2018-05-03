
import networkx as nx
import  StringUtility as su
import AbbreviatedNamesUtility as AN
import GraphUtility as gu
import OneHotEncodingUtility as heu

fxnGraph = nx.DiGraph()
anu=AN.Abbreviations()
fxnGraph.add_edge(anu.get(su.sanitize("abc")),anu.get(su.sanitize("def")))
fxnGraph.add_edge(anu.get(su.sanitize("def")),anu.get(su.sanitize("ghj")))

fxnGraph.add_edge(anu.get(su.sanitize("asd")),anu.get(su.sanitize("dds")))

fxnGraph.add_edge(anu.get(su.sanitize("sas")),anu.get(su.sanitize("sada")))

fxnGraph.add_edge(anu.get(su.sanitize("sas")),anu.get(su.sanitize("asdx")))

gu.visualize_to_dot(fxnGraph,"test2.dot")

gu.visualize_to_png("test2.dot","test2.png")

all_paths=gu.getAllPaths(fxnGraph,True)
#all_paths=gu.getAllOptimizedPaths(fxnGraph,True)

print("List size:",len(all_paths))
for sublist in all_paths:
  print(sublist)
  heu.getLabelEncoder(sublist)