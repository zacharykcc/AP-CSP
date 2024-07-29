# Zachary Wales
# Period 1
# An application (Capitalize16) that will capitalize an input name.  It will be 1,2 or 3 names.

def oneName(name):
    # Capitilizes first name
    name = name.lower()
    firstLet = name[0]
    firstLet = firstLet.upper()
    name = firstLet + name[1:]
    return name

def twoName(name):
    # Capitilizes first name
    name = name.lower()
    firstLet = name[0]
    firstLet = firstLet.upper()
    gap = name.find(" ")

    # Capitilizes second name
    secondLet = name[(gap+1):(gap+2)]
    secondLet = secondLet.upper()

    name = firstLet+name[1:gap]+" "+secondLet+name[gap+2:]
    return(name)

def threeName(name):
    # Capitilizes first name
    name = name.lower()
    firstLet = name[0]
    firstLet = firstLet.upper()
    gap = name.find(" ")
    firstName = firstLet+name[1:(gap+1)]
    # Capitilizes second name
    midEnd = name[gap+1:]
    secondLet = name[(gap+1):(gap+2)]
    secondLet = secondLet.upper()
    gap2 = midEnd.find(" ")
    middleName = secondLet+name[gap+2:(gap2+len(firstName)+1)]
    # Capitilizes third name
    third = name[(len(firstName))+gap2+1:]
    thirdLet = third[0]
    thirdLet = thirdLet.upper()
    lastName = thirdLet + third[1:]
    
    name = firstName+middleName+lastName
    return name
    
    
name = ""
done = False
firstHalf = ""

print("***Capitalizing Method***")

while done == False:
    name = input("Input name to be capitalized: ")
    name = name.strip()
# If the user is done
    if name.lower() == "done":
        done = True
        print("The End!")

    if done == False:
        space1 = name.find(" ")
        if space1 == -1:
            name = oneName(name)
            firstHalf = name[space1+1:]
        elif space1 > -1:
            firstHalf = name[space1+1:]
            
        space2 = firstHalf.find(" ")

        if space2 == -1 and space1 > -1:
            name = twoName(name)
        elif space2 > -1:
           name = threeName(name) 
        
        
        print(name)
        print("")
        print("")
