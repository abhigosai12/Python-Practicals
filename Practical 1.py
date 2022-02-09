# Student management system


College     =  int(input("Enter Your College Name : "))
Name        =  int(input("Enter Student Name : "))
Semester    =  int( input("Enter Student Semester : "))
Enrollment  =  int(input("Enter Enrollment Number : "))


Subjects    = {"oop", "java", "database"}
Subjectcode = ["11", "22", "33"]
oop         =  int(input("oop Marks : "))
java        =  int(input("java Marks : "))
database    =  int(input("database Marks : "))

Total = oop + java + database

average = (Total / 300) * 100

print("\n\t\tYOUR RESULT")
print("\t\tCOLLEGE     :",College)
print("\t\tNAME        :",Name)
print("\t\tENROLLMENT  :",Enrollment)
print("\t\tSUBJECT MARKS ")
print("\t\toop         :",oop)
print("\t\tjava        :",java)
print("\t\tdatabase    :",database)
print("\t\tTotal Marks :",Total)
print("\t\tPercentage  :",average)
