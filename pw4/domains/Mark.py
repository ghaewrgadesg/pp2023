#Creating the mark class
class Mark:
    def __init__(self,sID, mark):
        self.__studentID = sID
        self.__mark = mark
    #function for comparison
    def __lt__(self, other):
        return self.__mark < other.getMark()
   
    def __gt__(self, other):
        return self.__mark > other.getMark()
   
    def __eq__(self, other):
        return self.__mark == other.getMark()
    
    #return the value:
    def getSID(self):
        return self.__studentID
    def getMark(self):
        return self.__mark

    #Creating the setters
    def setSID(self,ID):
        self.__studentID = ID
    def setMark(self,mark):
        self.__mark = mark
    
