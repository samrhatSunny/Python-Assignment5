dt_studentMark = {}
def updateStudent():
    name = input("Enter student name")
    mark = int(input("Enter student marks"))
    dt_studentMark[name] = mark

def get_student():
    name = input("Enter student name")
    print(dt_studentMark.get(name,"Student name not found"))