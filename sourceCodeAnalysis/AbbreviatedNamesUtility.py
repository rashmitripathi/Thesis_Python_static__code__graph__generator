
class Abbreviations():
    shortNames={}
    counter=0
    def __init__(self):
        Abbreviations.counter = 0
        pass

    def update(self,str):
        if(not Abbreviations.shortNames.__contains__(str)):
            Abbreviations.counter = Abbreviations.counter + 1
            Abbreviations.shortNames[str]="f"+Abbreviations.counter.__str__()


    def get(self, str):
        if (not Abbreviations.shortNames.__contains__(str)):
            self.update(str)
        return Abbreviations.shortNames.get(str)