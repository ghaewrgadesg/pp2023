from datetime import datetime    
import re
import math
import numpy as np
import curses
from curses import wrapper
#creating the student class
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
                    print("The mark of {} in the course {} is: {}".format(student.getName(), self.__name, i.getMark()))
                    return True
        except KeyError:
            return False
        #return if the student does not have a mark for this course
        return False
    def display(self):
        return "ID: {} - Name: {}".format(self.__id,self.__name)

#the functions
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

#sort student list based on GPA
def sortStudentList(sList):
    return np.sort(sList)

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

#check the mark of a singular student
def checkStudentMark(sList, cList):
    studentToCheck = 0
    courseToCheck = 0
    stdscr = curses.initscr()
    stdscr.refresh()
    line = 0
    #wrapper stuffs
    curses.cbreak()
    stdscr.keypad(1)
    curses.noecho()
    #end of wrapper stuffs
    while courseToCheck == 0:
        for i in cList:
            stdscr.addstr(line, 0, "{} {}".format(i.getID(), i.getName()))
            line += 1
        stdscr.refresh()
        line += 1
        stdscr.addstr(line, 0, "Input the course's ID: ")
        line += 2
        tBoxWin = curses.newwin(1, 10, line ,2)
        tBox = Textbox(tBoxWin)
        rectangle(stdscr,line-1,1, line + 1, 12)
        line += 2
        stdscr.refresh()
        tBox.edit()
        courseID = tBox.gather().rstrip()
        for i in cList:
            if i.getID() == courseID:
                courseToCheck = i
                break
        if courseToCheck == 0:
            stdscr.addstr(line, 0, "Course ID not found")
            line = 0
            stdscr.getch()
            stdscr.erase()
    stdscr.erase()
    line = 0
    stdscr.refresh()        
    while studentToCheck == 0:
        for i in sList:
            stdscr.addstr(line, 0, "{} {}".format(i.getID(), i.getName()))
            line += 1
        stdscr.refresh()
        line += 1
        stdscr.addstr(line, 0, "Input the student's ID: ")
        line += 2
        tBoxWin = curses.newwin(1, 10, line ,2)
        tBox = Textbox(tBoxWin)
        rectangle(stdscr,line-1,1, line + 1, 12)
        line += 2
        stdscr.refresh()
        tBox.edit()
        studentID = tBox.gather().rstrip()
        for i in sList:
            if i.getID() == studentID:
                studentToCheck = i
                break
        if studentToCheck == 0:
            stdscr.addstr(line, 0, "student ID not found")
            line = 0
            stdscr.getch()
            stdscr.erase()
    stdscr.erase()
    line = 0
    stdscr.refresh()
    if courseToCheck.checkMark(studentToCheck):         
        stdscr.addstr(line, 0, courseToCheck.checkMark(studentToCheck))
    line += 1
    stdscr.addstr(line, 0, "\nPress any key to continue...", curses.A_BOLD)
    stdscr.getch()
    stdscr.erase()
    #wrapper stuffs
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    #end of wrapper
    curses.endwin()

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

#check the mark of all student in a chosen course
#check the mark of all student in a chosen course
def checkAllStudent(sList, cList):
    courseToCheck = 0
    stdscr = curses.initscr()
    stdscr.refresh()
    line = 0
    #wrapper stuffs
    curses.cbreak()
    stdscr.keypad(1)
    curses.noecho()
    #end of wrapper stuffs
    while courseToCheck == 0:
        for i in cList:
            stdscr.addstr(line, 0, "{} {}".format(i.getID(), i.getName()))
            line += 1
        stdscr.refresh()
        line += 1
        stdscr.addstr(line, 0, "Input the course's ID: ")
        line += 2
        tBoxWin = curses.newwin(1, 10, line ,2)
        tBox = Textbox(tBoxWin)
        rectangle(stdscr,line-1,1, line + 1, 12)
        line += 2
        stdscr.refresh()
        tBox.edit()
        courseID = tBox.gather().rstrip()
        for i in cList:
            if i.getID() == courseID:
                courseToCheck = i
                break
        if courseToCheck == 0:
            stdscr.addstr(line, 0, "Course ID not found")
            line = 0
            stdscr.erase()
    stdscr.erase()
    line = 0
    stdscr.refresh()        
    stdscr.addstr(line, 0, "Students' Marks for {}: ".format(courseToCheck.getName()))
    line += 1
    for i in sList:
        if courseToCheck.checkMark(i):
            stdscr.addstr(line, 0, courseToCheck.checkMark(i))
            line += 1
    stdscr.addstr(line, 0, "\nPress any key to continue...", curses.A_BOLD)
    stdscr.getch()
    stdscr.erase()
    #wrapper stuffs
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    #end of wrapper stuffs
    curses.endwin()

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

#display the students using curse
def displayStudents(sList):
    # Initialize the screen
    stdscr = curses.initscr()
    stdscr.refresh()
    stdscr.addstr('Student list:')
    line = 1
    for i in sList:
        stdscr.addstr(line, 0, i.display())
        line = line + 1

    stdscr.refresh()

    stdscr.addstr(line, 0, "\nPress any key to continue...", curses.A_BOLD)
    stdscr.getch()
    curses.endwin()

#display the courses using curses
def displayCourses(cList):
    # Initialize the screen
    stdscr = curses.initscr()
    stdscr.refresh()
    stdscr.addstr('Course list:')
    line = 1
    for i in cList:
        stdscr.addstr(line, 0, i.display())
        line = line + 1

    stdscr.refresh()

    stdscr.addstr(line, 0, "\nPress any key to continue...", curses.A_BOLD)
    stdscr.getch()
    curses.endwin()

#Initializing the student lists 
studentNo = getStudentNo()
courseNo = getCourseNo()
studentList = [Student(0,0,0) for i in range(studentNo)]
courseList = [Course(0,0) for i in range(courseNo)]
#test students
#studentList = [Student("Test1", "Malo", "10-10-2003"), Student("Test2", "Mulo", "20-10-1990")]
#courseList = [Course("MST", "Mystical"), Course("BRG", "Barrage")]

#get the students and courses infos
for i in studentList:
   i.input()  
for i in courseList:
   i.input()
studentList = np.array(studentList)
#the menu
while True:
    print("""---------------------------------------
1.Show the student list
2.Show the course list
3.Check the mark of a student in a course
4.Check the mark of all students in a course
5.Input the mark of a student in a course
6.Input the mark of all students in a course
7.Exit
""")
    try:
        choice = int(input("Enter a number: "))
    except ValueError:
        continue
    match choice:
        case 1: 
            displayStudents(studentList)
            pause = input("Enter to continue: ")
            print("\n-----------------------------------")
        case 2:
            for i in courseList:
                i.display()
            pause = input("Enter to continue: ")
            print("\n-----------------------------------")
        case 3:
            checkStudentMark(studentList,courseList)
            pause = input("Enter to continue: ")
            print("\n-----------------------------------")     
        case 4:
            checkAllStudent(studentList, courseList)
            pause = input("Enter to continue: ")
            print("\n-----------------------------------")  
                         
        case 5:
            inputStudentMark(studentList,courseList)
            studentList = sortStudentList(studentList)
            pause = input("Enter to continue: ")
            print("\n-----------------------------------")  
        case 6:
            inputAllStudents(studentList,courseList)
            studentList = sortStudentList(studentList)
            pause = input("Enter to continue: ")
            print("\n-----------------------------------")          
        case 7: 
            break
        case _:
            continue

#for i in courseList:
#    for g in studentList:
#        i.inputMark(g)
#for i in courseList:
#    for g in studentList:
#        print("{}'s mark for the course is: {}".format(g.getName(), i.checkMark(g)))
#I AM IN PAINAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
