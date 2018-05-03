
class callerMatrix(object):

 def __init__(self):
     pass

 def clean(obj):
    newObj={}
    for k, v in obj.items():
        k=k.replace("Fxn:","")
        for value in v:
          value = value.split("(")[0]
          newObj[k]=v
    return newObj

 def cleanInput(self,obj):
    newObj=self.clean(obj)
    for k, v in newObj.items():
        print("after sanitazation input:")
        print(k,v)









