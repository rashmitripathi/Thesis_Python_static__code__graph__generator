from anytree import Node, RenderTree
import re

udo = Node("Udo")
marc = Node("Marc", parent=udo)
lian = Node("Lian", parent=marc)
dan = Node("Dan", parent=udo)
jet = Node("Jet", parent=dan,)
jan = Node("Jan", parent=dan)
joe = Node("Joe", parent=dan)
jet = Node("Jet", parent=udo)


for pre, fill, node in RenderTree(udo):
    print("%s%s" % (pre, node.name))


print(dan.children)


str="lksdkfdlj(kjkdjshfjhs"
str1="26829)()ffjh"

print(str.__contains__("("))
regex_num = re.compile('\d+')
str1 = re.sub("\d|\)|\(+", "",str1)
print(str1)