# Period 1
# Zachary Wales
# An application that will prompt for an input of someone's full name and then capitalize all of the 3 names in the string

# Variables
name = ""
done = False

# Start of name
start1 = 0
start2 = 0
start3 = 0

# End of name
end1 = 0
end2 = 0
end3 = 0

# The name
name1 = ""
name2 = ""
name3 = ""

while not done:
    name = input("What is the name? ")
    if name == "done" or name == "Done":
        print("The End!")
        done = True
    else:
        # Find("What is being searched for", Where to start searching(optional), Where to end searching(optional))
        name = name.lower()

        start1 = name[0]
        start1 = start1.upper()
        end1 = name.find(" ")
        name1 = start1+name[1:end1]
        print(name1, end=" ")

        start2 = name[end1+1]
        start2 = start2.upper()
        end2 = name.find(" ", end1+1)
        name2 = start2+name[end1+2:end2]
        print(name2, end=" ")

        start3 = name[end2+1]
        start3 = start3.upper()
        end3 = name.find(" ", end2+1)
        name3 = start3+name[end2+2:]
        print(name3)
input("")
