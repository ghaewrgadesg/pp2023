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