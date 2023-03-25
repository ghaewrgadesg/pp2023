from domains import Mark, Student, Course
import math
import numpy as np
#sortList
def sortStudentList(sList):
    return np.sort(sList)
#Input the mark of a singular student
def inputStudentMark(sList, cList):
    courseToCheck = 0
    studentToCheck = 0    
    for i in cList:
        print("{} {}".format(i.getID(), i.getName()))
    while courseToCheck == 0:
        courseID = input("Input the course's ID: ")
        for i in cList:
            if i.getID() == courseID:
                courseToCheck = i
                break
        if courseToCheck == 0:
            print("Course ID not found")
    for i in sList:
        print("{} {}".format(i.getID(), i.getName()))
    while studentToCheck == 0:
        studentID = input("Input the student's ID: ")
        for i in sList:
            if i.getID() == studentID:
                studentToCheck = i
                break
        if studentToCheck == 0:
            print("Wrong ID")
    courseToCheck.inputMark(studentToCheck)
    studentToCheck.calcGPA(cList)

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


#input the mark of all students in a chosen course
def inputAllStudents(sList, cList):
    courseToCheck = 0
    studentToCheck = 0    
    for i in cList:
        print("{} {}".format(i.getID(), i.getName()))
    while courseToCheck == 0:
        courseID = input("Input the course's ID: ")
        for i in cList:
            if i.getID() == courseID:
                courseToCheck = i
                break
        if courseToCheck == 0:
            print("Course ID not found")
    for i in sList:
        courseToCheck.inputMark(i)
        i.calcGPA(cList)

#get number of students
def getStudentNo():
    #loop getting the number until it is in the desired format (positive integer)
    while True: 
        try: 
            studentNo = int(input("Input the number of students: "))
            if studentNo > 0:
                break
        except ValueError:
            continue
    return studentNo

def getCourseNo():
    #loop getting the number until it is in the desired format (positive integer)
    while True: 
        try: 
            courseNo = int(input("Input the number of courses: "))
            if courseNo > 0:
                break
        except ValueError:
            continue
    return courseNo