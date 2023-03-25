import math
import numpy as np
import curses
from curses.textpad import rectangle, Textbox
from domains import Mark, Student, Course
from input import sortStudentList,inputStudentMark,getStudentNo,getCourseNo, inputAllStudents
from output import  checkStudentMark, checkAllStudent, displayStudents, displayCourses

#Initializing the student lists 
studentNo = getStudentNo()
courseNo = getCourseNo()
studentList = [Student(0,0,0) for i in range(studentNo)]
courseList = [Course(0,0) for i in range(courseNo)]
while True:
    try:
        error = 0
        with open("Student.txt", 'r') as f:
            studentNo = sum(1 for line in open('Student.txt'))
            studentList = []
            for i in range(studentNo):
                info = f.readline().rstrip().split('/')
                studentList.append(Student(info[0],info[1],info[2]))
        error = 1
        with open("Course.txt", 'r') as f:
            courseNo = sum(1 for line in open('Course.txt'))
            courseList = []
            for i in range(courseNo):
                info = f.readline().rstrip().split('/')
                courseList.append(Course(info[0],info[1]))
        error = 2
        with open("Mark.txt", 'r') as f:
            markList = []
            for i in range(courseNo):
                info = f.readline().rstrip().split('/')
                for g in info:
                    markInfo = g.split(',')
                    courseList[i].appendMark(Mark(markInfo[0], int(markInfo[1])))
        break

    except FileNotFoundError:
        match error:
            case 0:
                studentNo = getStudentNo()
                studentList = [Student(0,0,0) for i in range(studentNo)]
                for i in studentList:
                    i.input()  
                    print('-----------------------------------------')
                    with open("Student.txt", "w") as f:
                        for i in studentList:
                            f.write("{}/{}/{}\n".format(i.getID(),i.getName(),str(i.getDOB()))) 
            case 1:
                courseNo = getCourseNo()
                courseList = [Course(0,0) for i in range(courseNo)]
                for i in courseList:
                    i.input()
                    print('-----------------------------------------')
                with open("Course.txt", "w") as f:
                    for i in courseList:
                        f.write("{}/{}\n".format(i.getID(),i.getName())) 
            case 2:
                break


#get the students and courses infos
#for i in studentList:
#   i.input()  
#for i in courseList:
#   i.input()
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
            print("\n-----------------------------------")
        case 2:
            displayCourses(courseList)
            print("\n-----------------------------------")
        case 3:
            checkStudentMark(studentList,courseList)
            print("\n-----------------------------------")     
        case 4:
            checkAllStudent(studentList, courseList)
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