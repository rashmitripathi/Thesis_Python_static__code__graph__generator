import json
import os


def dumpDataFromList(inputmatrix,cluster,idkeyword,filename):
 save_path = 'E:/Thesis/sourceCodeAnalysis/clusteringUI/'
 completeName = os.path.join(save_path, filename + ".json")
 data = {}
 group={}
 data['nodes'] = []
 counter=1
 for x in cluster[:]:
     print(x)
     temp = {"id": idkeyword + str(counter), "group": int(x)}
     data['nodes'].append(temp)
     if x in group.keys():
         group[x].append(x)
     else:
         group[x] = [x, ]
     counter = counter + 1

 data['links']=[]

 row=1
 #print("input matrix is :fjf",inputmatrix)
 for sublst in inputmatrix:
     col = 1
     for item in sublst:
         if(float(item) > 0.5 and row != col):
            #print("adddgsdgsg:",row,col,item)
            value=float(item)*10
            temp = {"source": idkeyword+str(row),"target": idkeyword+str(col) , "value": value}
            data['links'].append(temp)
         col = col + 1
     row += 1


 with open(completeName, 'w') as outfile:
    json.dump(data, outfile)

#dumpDataFromList([[1,0.5,0.5],[0.5,1,0.5],[0.5,0.5,1]],[1,2,0,0,1,2],"p","data")