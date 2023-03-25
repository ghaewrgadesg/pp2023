from domains import Student, Course,Mark
from input import getStudentNo, getCourseNo
try:
    error = 0
    with open("Student.txt", 'r') as f:
        studentNo = sum(1 for line in open('Student.txt'))
        studentList = []
        for i in range(studentNo):
            info = f.readline().rstrip().split('/')
            print(info)
            studentList.append(Student(info[0],info[1],info[2]))
    error = 1
    with open("Course.txt", 'r') as f:
        courseNo = sum(1 for line in open('Course.txt'))
        courseList = []
        for i in range(courseNo):
            info = f.readline().rstrip().split('/')
            courseList.append(Course(info[0],info[1]))
    with open("Mark.txt", 'r') as f:
        markList = []
        for i in range(courseNo):
            info = f.readline().rstrip().split('/')
            for g in info:
                markInfo = g.split(',')
                courseList[i].appendMark(Mark(markInfo[0], int(markInfo[1])))
    
except FileNotFoundError:
    match error:
        case 0:
            studentNo = getStudentNo()
            studentList = [Student(0,0,0) for i in range(studentNo)]
            for i in studentList:
               i.input()  
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
            pass
for i in studentList:
    print(i.display())
