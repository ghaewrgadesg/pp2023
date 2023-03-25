from datetime import datetime    
import numpy as np
import re

class Student:
    #initializing the default id, name and DOB
    def __init__(self,id,name,DOB):
        self.__id = id
        self.__name = name
        self.__DOB = DOB
        self.__GPA = -1
    
    #compare students based on their GPA:
    def __lt__(self, other):
        return self.__GPA < other.getGPA()
   
    def __gt__(self, other):
        return self.__GPA > other.getGPA()
   
    def __eq__(self, other):
        try:
            return self.__GPA == other.getGPA()
        except:
            return False
    #creating setters
    def setID(self, ID):
        #creating the ID pattern and check if the ID is of the correct pattern
        idPattern = re.compile("^B[AI]\d{2}-\d{3}$")
        if idPattern.match(ID):
            self.__id = ID
            return True
        else:
            return False
        
    def setName(self, name):
        self.__name = name
        return True

    def setDOB(self, DoB):
        try:
            #check if the inputted DOB is of the correct format and set it
            test = datetime.strptime(DoB,"%d-%m-%Y")
            self.__DOB=  DoB
            return True            
        except (ValueError, TypeError):
            return False

    #Creating the observer
    def getID(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def getDOB(self):
        return self.__DOB
    
    def getGPA(self):
        if self.__GPA >= 0:
            return self.__GPA
        else:
            return 0
        
    #get user to input the values
    def input(self):
        while True:
            ID = input("Input the student's ID: ")
            if not self.setID(ID):
                print("Wrong ID's format(BIXX-XXX) ")
                continue
            name = input("Input the student's name: ")
            if not self.setName(name):
                print("Wrong name format")
                continue
            DoB = input("Input the student's birthday (DD-MM-YYYY): ")
            if not self.setDOB(DoB):
                print("Wrong birthday's format")
                continue
            break

    #Function to calculate GPA ?
    def calcGPA(self, cList):
        marks = np.array([])
        for i in cList:
            for g in i.getMarkList():
                if g.getSID() == self.__id:
                    marks = np.append(marks, [g.getMark()])
                    break
        GPA = np.average(marks)
        self.__GPA = GPA
        return True


    #display the value
    def display(self):
        return "ID: {} - Name: {} - Birthday: {} - GPA: {}".format(self.__id,self.__name,self.__DOB, self.getGPA())