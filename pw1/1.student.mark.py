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
        courseList[i][1] = input("Enter the course number {} name: ".format(i+1))
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
        studentName = input("Enter the student number {} name: ".format(i+1))
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
    for i in range(len(studentList)):
        #run through the courses
        for g in range(len(courseList)):
            try:
                while True:
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
            print("Student ID: {}".format(studentID))
            break
        except (ValueError,IndexError):
            continue
    listCourses(courseList)
    #Choose the course to get the grade of the chosen student
    while True: 
        try: 
            option = int(input("Choose the course: "))
            courseID = courseList[option-1][0] 
            print("Course ID: {}".format(courseID))
            break
        except (ValueError,IndexError):
            continue
    print("The mark of {} in the course {} is: {}".format(studentList[studentID-1][1],courseList[courseID-1][1],markList[studentID-1][courseID-1]))
courseNo = getCourseNo()
courses = getCourseInfo(courseNo)
studentNo = getStudentNo()
students = getStudentInfo(studentNo)
marks = getStudentMarks(students, courses)
#the menu
while True:
    print("""---------------------------------------
1.Show the student list
2.Show the course list
3.Check the mark of a student
4.Exit
""")
    try:
        choice = int(input("Enter a number: "))
    except ValueError:
        continue
    match choice:
        case 1: 
            listStudents(students)
            pause = input("Enter to continue: ")
            print("\n-----------------------------------")
        case 2:
            listCourses(courses)
            pause = input("Enter to continue: ")
            print("\n-----------------------------------")
        case 3:
            studentMark(students, courses, marks)
            pause = input("Enter to continue: ")
            print("\n-----------------------------------")            
        case 4: 
            break
        case _:
            continue