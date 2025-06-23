dt_studentMark = {"Amol":55,"Vishal":65,"Amit":60,"Shreyas":75,"Pranav":59}
strName = input("Enter student name ")
if strName in dt_studentMark:
    print(dt_studentMark[strName])
else:
    print("Student name not found")