#Period 1
#Zachary Wales
# An application that will ask the user for the number of grades to input.  The user will input that many grades
# and the program will store them in a list called grades. Each grade must be 0-100.
# The program will then use 3 procedures that you will write called
# getMin(myList), getMax(myList), and getAvg(myList) to display the minimum, maximum, and average of the inputted grades. 

# 3 Procedures

    # Gets the min
def getMin(myList):
    length = len(myList)
    minnum = myList[0]
    for count in range(length):
        if myList[count] < minnum:
            minnum = myList[count]
        count = count + 1
    return minnum

    # Gets the max
def getMax(myList):
    length = len(myList)
    maximum = myList[0]
    for count in range(length):
        if myList[count] > maximum:
            maximum = myList[count]
        count = count + 1
    return maximum

    # Gets the Average
def getAvg(myList):
    length = len(myList)
    total = 0
    average = 0
    for count in range(length):
        total = total + myList[count]
        count = count + 1 
    average = total/length
    return average


grades = []
grade = 0



# Number of Grades
numGrades = int(input("How many grades would you like to input? "))
while numGrades <= 0:
    print("That number of grades is invalid, please enter a number of grades greater than 0")

# Inputs all of the Grades    
for count in range(numGrades):
    count = count + 1
    grade = float(input("Enter Grade "+str(count)+str(": ")))
    while grade > 100 or grade < 0:
        print("That grade is unacceptable, please enter a grade from 0-100")
        grade = float(input("Enter Grade "+str(count)+str(": ")))
    grades.append(grade)

# Prints Average, Maximum, and Minimum
print("There are "+str(numGrades)+" grades.")
print("The maximum grade is: "+str(round(getMax(grades), 1)))
print("The minimum grade is: "+str(round(getMin(grades), 1)))
print("The average grade is: "+str(round(getAvg(grades), 1)))
