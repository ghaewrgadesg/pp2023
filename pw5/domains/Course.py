import math
from .Mark import Mark
#Creating the course class
class Course:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__mark = []

    #return the values of variables within the class
    def getID(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def getMarkList(self):
        return self.__mark
    
    #make the user input the values of variables within the class    
    def setID(self,ID):
        self.__id = ID

    def setName(self, name):
        self.__name = name

    def appendMark(self, mark):
        self.__mark.append(mark)


    #Run all 2 function above
    def input(self):
        ID = input("Input the course's ID: ")
        name = input("Input the course's name: ")
        self.setID(ID)
        self.setName(name)

    #The function to input the mark of the students
    def inputMark(self, student):
        studentID = student.getID()
        mark = -1
        #make sure that the mark is of the correct format
        while mark <0 or mark >20: 
            try: 
                mark = float(input("Enter {}: {}'s mark: ".format(student.getID(), student.getName())))
                mark = math.floor(mark*10)/10
            except ValueError:
                continue
        #constructing the mark class containing the mark info        
        if len(self.__mark) > 0:
            #if mark is not empty check to see if the student already had a grade and just replace it
            try:
                for i in self.__mark:
                    if i.getSID() == studentID:
                        i.setMark(mark)
                        return True
            except KeyError:
                self.__mark.append(Mark(studentID, mark))
                return True
        #creating a new entry for a student
        self.__mark.append(Mark(studentID, mark))
        return True

    #function to check the mark of a student
    def checkMark(self, student):
        #sift through the mark list to see if the student has a mark
        try:
            for i in self.__mark:
                if i.getSID() == student.getID():
                    return "The mark of {} in the course {} is: {}".format(student.getName(), self.__name, i.getMark())
        except KeyError:
            return False
        #return if the student does not have a mark for this course
        return False
    def display(self):
        return "ID: {} - Name: {}".format(self.__id,self.__name)