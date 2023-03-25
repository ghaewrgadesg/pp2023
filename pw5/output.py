from domains import Mark, Student, Course
import curses
from curses.textpad import rectangle, Textbox



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
    stdscr.erase()
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
    stdscr.erase()
    curses.endwin()