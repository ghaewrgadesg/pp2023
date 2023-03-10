from datetime import datetime    
#creating the student class
class Student:
    #initializing the default id, name and DOB
    def __init__(self,id,name,DOB):
        self.__id = id
        self.__name = name
        self.__DOB = DOB
    #return the values of variables within the class
    def giveID(self):
        return self.__id
    
    def giveName(self):
        return self.__name
    
    def giveDOB(self):
        return self.__DOB
    #Input the values of variables
    def getID(self):
        self.__id = input("Input the student's ID: ")

    def getName(self):
        self.__name = input("Enter the student's name: ")

    def getDOB(self):
        while True:
            try:
                self.__DOB=  input("Enter the DOB(DD-MM-YYYY): ") 
                #check if the inputted DOB is of the correct format
                test = datetime.strptime(self.__DOB,"%d-%m-%Y")
                break
            except ValueError:
                continue
    #Run all 3 function above
    def input(self):
        self.getID()
        self.getName()
        self.getDOB()
    #display the value
    def display(self):
        print("ID: {}; Name: {}; Birthday: {}".format(self.__id,self.__name,self.__DOB))

class Course:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__mark = []

    #return the values of variables within the class
    def giveID(self):
        return self.__id
    
    def giveName(self):
        return self.__name
    
    #make the user input the values of variables within the class    
    def getID(self):
        self.__id = input("Input the course's ID: ")

    def getName(self):
        self.__name = input("Enter the course's name: ")

    #Run all 2 function above
    def input(self):
        self.getID()
        self.getName()

    #The function to input the mark of the students
    def inputMark(self, student):
        studentID = student.giveID()
        mark = -1
        #make sure that the mark is of the correct format
        while mark <0 or mark >10: 
            try: 
                mark = float(input("Enter {}-{}'s mark: ".format(student.giveID(), student.giveName())))
            except ValueError:
                continue
        #adding the dictionary with the student's info        
        if len(self.__mark) > 0:
            #if mark is not empty check to see if the student already had a grade and just replace it
            try:
                for i in self.__mark:
                    if i['ID'] == studentID:
                        i['mark'] = mark
                        return
            except KeyError:
                self.__mark.append({'ID': studentID, 'mark': mark})
                return
        #creating a new entry for a student
        self.__mark.append({'ID': studentID, 'mark': mark})

    #function to check the mark of a student
    def checkMark(self, student):
        #sift through the mark list to see if the student has a mark
        try:
            for i in self.__mark:
                if i['ID'] == student.giveID():
                    print("The mark of {} in the course {} is: {}".format(student.giveName(), self.__name, i['mark']))
                    return
        except KeyError:
            print("THERE IS NO MARK IN THIS COURSE")
            return
        #return if the student does not have a mark for this course
        print("NOT FOUND")
    def display(self):
        print("ID: {}; Name: {}".format(self.__id,self.__name))

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
    courseToCheck = 0
    studentToCheck = 0
    while courseToCheck == 0:
        for i in cList:
            print("{} {}".format(i.giveID(), i.giveName()))
        courseID = input("Input the course's ID: ")
        for i in cList:
            print(i.giveID() == courseID)
            if i.giveID() == courseID:
                courseToCheck = i
                break
        if courseToCheck == 0:
            print("Course ID not found")
    
    for i in sList:
        print("{} {}".format(i.giveID(), i.giveName()))
    while studentToCheck == 0:
        studentID = input("Input the student's ID: ")
        for i in sList:
            if i.giveID() == studentID:
                studentToCheck = i
                break
        if studentToCheck == 0:
            print("Student ID not found")
    courseToCheck.checkMark(studentToCheck)
#Input the mark of a singular student
def inputStudentMark(sList, cList):
    courseToCheck = 0
    studentToCheck = 0    
    for i in cList:
        print("{} {}".format(i.giveID(), i.giveName()))
    while courseToCheck == 0:
        courseID = input("Input the course's ID: ")
        for i in cList:
            if i.giveID() == courseID:
                courseToCheck = i
                break
        if courseToCheck == 0:
            print("Course ID not found")
    for i in sList:
        print("{} {}".format(i.giveID(), i.giveName()))
    while studentToCheck == 0:
        studentID = input("Input the student's ID: ")
        for i in sList:
            if i.giveID() == studentID:
                studentToCheck = i
                break
        if studentToCheck == 0:
            print("Student ID not found")
    courseToCheck.inputMark(studentToCheck)

#check the mark of all student in a chosen course
def checkAllStudent(sList, cList):
    courseToCheck = 0
    while courseToCheck == 0:
        for i in cList:
            print("{} {}".format(i.giveID(), i.giveName()))
        courseID = input("Input the course's ID: ")
        for i in cList:
            print(i.giveID() == courseID)
            if i.giveID() == courseID:
                courseToCheck = i
                break
        if courseToCheck == 0:
            print("Course ID not found")
    for i in sList:
        courseToCheck.checkMark(i)

#input the mark of all students in a chosen course
def inputAllStudents(sList, cList):
    courseToCheck = 0
    studentToCheck = 0    
    for i in cList:
        print("{} {}".format(i.giveID(), i.giveName()))
    while courseToCheck == 0:
        courseID = input("Input the course's ID: ")
        for i in cList:
            if i.giveID() == courseID:
                courseToCheck = i
                break
        if courseToCheck == 0:
            print("Course ID not found")
    for i in sList:
        courseToCheck.inputMark(i)

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
            for i in studentList:
                i.display()
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
            pause = input("Enter to continue: ")
            print("\n-----------------------------------")  
        case 6:
            inputAllStudents(studentList,courseList)
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
#        print("{}'s mark for the course is: {}".format(g.giveName(), i.checkMark(g)))
#I AM IN PAINAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
