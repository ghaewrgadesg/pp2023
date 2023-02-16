from datetime import datetime    
import csv
#function to get the amount of students
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
def getCourseInfo(courseNo):
    #create the courseList
    courseList =[[0 for i in range (2)] for i in range (courseNo)]
    for i in range(courseNo):
        #auto put the ids        
        courseList[i][0] = i + 1
        #put the course's name 
        courseList[i][1] = input("Enter the course's name: ")
    return courseList
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
#function to get the student infos id, name dob
def getStudentInfo(studentNo):
    studentList =[]
    for i in range(studentNo):
        #create the list to hold the individual student info
        studentList.append([])
        #auto put the ids        
        id= i+1
        studentList[i].append(id)
        studentName = input("Enter the student's name: ")
        studentList[i].append(studentName)
        while True:
            try:
                DOB=  input("Enter the DOB(DD-MM-YYYY): ") 
                #check if the inputted DOB is of the correct format
                test = datetime.strptime(DOB,"%d-%m-%Y")
                break
            except ValueError:
                continue
        studentList[i].append(DOB)
    return studentList
def getStudentMarks(studentList, courseList):
    markList = [[0 for i in range (len(courseList))] for i in range (len(studentList))]
    #run through the students
    print("course: {}; student: {}".format(len(courseList),len(studentList)))
    for i in range(len(studentList)):
        #run through the courses
        print("lenght: {}".format(len(courseList)))
        for g in range(len(courseList)):
            try:
                while True:
                    print("i is: {}; g is: {}".format(i,g))
                    markList[i][g] = float(input("Input the mark of the course {} for {}: ".format(courseList[g][1],studentList[i][1])))
                    if markList[i][g] > 0:
                        break
            except ValueError:
                continue
    
    return markList
def listStudents(studentList):
    #if u don't get this ur cringe
    for i in range (len(studentList)):
        print("{}.{} {}".format(studentList[i][0],studentList[i][1],studentList[i][2]))

def listCourses(courseList):
    for i in range (len(courseList)):
        print("{}.{} ".format(courseList[i][0],courseList[i][1]))
def studentMark(studentList, courseList,markList):
    listStudents(studentList)
    #show the student list and let the user choose the student
    while True: 
        try: 
            option = int(input("Choose the student you wish to see the grade of: "))
            studentID = studentList[option-1][0] 
            break
        except (ValueError,IndexError):
            continue
    listCourses(courseList)
    #Choose the course to get the grade of the chosen student
    while True: 
        try: 
            option = int(input("Choose the course: "))
            courseID = courseList[option-1][0] 
            break
        except (ValueError,IndexError):
            continue
    print("The mark of {} in the course {} is: {}".format(studentList[studentID-1][1],courseList[courseID-1][1],markList[studentID][courseID]))
courseNo = getCourseNo()
courses = getCourseInfo(courseNo)
print(len(courses))
studentNo = getStudentNo()
students = getStudentInfo(studentNo)
marks = getStudentMarks(students, courses)
studentMark(students,courses, marks)