# Period 1
# Zachary Wales
# A computer program given the first and second quarter grades will calculate the semester grade needed to get the desired grade.

# Requirement 2 Comments and Header
# Requirement 7, Different data types
# Requirement 11, Run without errors

# Requirement 1 Title
print("!*------Welcome to the Semester Exam Grade Calculator!------*!")

# ---- Variables
finished = False
fQtr = 0
sQtr = 0
done2 = False
semA = 0
semB = 0
semC = 0
semD = 0
useless = 0
    
# ---- Spacing
def spaces():
    print()
    print("--------------------------------------")
    print()
# ---- Main Loop


# Requirement 3, while loop, Requirement 6 Continuous Run

# ---- Gets the user's input for grades
while not finished:
    fQtr = float(input("What is your first quarter grade percentage: "))
    
# Requirement 8, Error Proofing

    while fQtr > 100 or fQtr < 0:
        print("***That grade is unacceptable***")
        fQtr = float(input("What is your first quarter grade percentage: "))

    sQtr = float(input("What is your second quarter grade percentage: "))
    while sQtr > 100 or sQtr < 0:
        print("***That grade is unacceptable***")
        sQtr = float(input("What is your second quarter grade percentage: "))
    spaces()
    print("First Qtr Grade: "+str(fQtr)+"\tSecond Qtr Grade: "+str(sQtr))
    spaces()

# Requirement 10, Calculation of grades correctly

# ---- Calculations
    fQtr = fQtr*.4
    sQtr = sQtr*.4
    sem = fQtr+sQtr
    semA = round((5*(89.5-sem)), 1)
    semB = round((5*(79.5-sem)), 1)
    semC = round((5*(69.5-sem)), 1)
    semD = round((5*(59.5-sem)), 1)
    
# ---- Printing and if, for extra credit statements
# Requirement 9, Extra Credit
    if semA > 100:
        print("You are going to need some extra credit to get a A")
    elif semA < 0:
        print("You are guaranteed to get a A")
    print("To get an A, you will need a "+str(semA))
    spaces()

    if semB > 100:
        print("You are going to need some extra credit to get a B")
    elif semA < 0:
        useless = useless + 1
    elif semB < 0:
        print("You are guaranteed to get a B")
    print("To get an B, you will need a "+str(semB))
    spaces()

    if semC > 100:
        print("You are going to need some extra credit to get a C")
    elif semA < 0:
        useless = useless + 1
    elif semB < 0:
        useless = useless + 1
    elif semC < 0:
        print("You are guaranteed to get a C")
    print("To get an C, you will need a "+str(semC))
    spaces()

    if semD > 100:
        print("You are going to need some extra credit to get a D")
    elif semA < 0:
        useless = useless + 1
    elif semB < 0:
        useless = useless + 1
    elif semC < 0:
        useless = useless + 1
    elif semD < 0:
        print("You are guaranteed to get a D")
    print("To get an D, you will need a "+str(semD))
    spaces()
    
    done = input("Would you like to calculate another grade? ")




# ---- If the user is done calculating
        
# Requirement 4, if(else)
# Requirement 5, Logic
# Requirement 6, Continuous Run
    while not done2:
        if done == "Yes" or done == "y" or done == "Y" or done == "YES":
            finished = False
            done2 = True
        elif done == "No" or done == "n" or done == "N" or done == "NO" or done == "no":
            finished = True
            done2 = True
        else:
            print("Response Invalid")
            print("For Yes respond with Yes, y, yes, Y, or YES")
            print("For No respond with No, n, no, N, or NO")
            done = input("Would you like to calculate another grade? ")
    done2 = False
print()
print("Thank you and Good Luck on your exam!")


