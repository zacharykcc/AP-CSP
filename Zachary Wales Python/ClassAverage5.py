# Zachary Wales
# Period 1
# A program using a while loop that calculate
# the class average of a number of grades for a particular class.
# Due 10/12/2022


i = 1
grade = 0
added = 0
average = 0
students = int(input("How many students are in the class? "))

#Makes sure that the number of students is valid
if students <= 0:
    while students <= 0:
        print("That number of students is unacceptable")
        students = int(input("How many students are in the class? "))
        
# Makes sure all students have a valid grade
while i <= students:
    grade = float(input("Input Grade "+str(i)+" : "))
    if grade > 100:
        print("That grade is unacceptable")
    elif grade < 0:
        print("That grade is unacceptable")
    else:   
        added = added + grade
        i= i+1

# Calculates average and prints
average = added/students
print("The class average is "+str(average))    
