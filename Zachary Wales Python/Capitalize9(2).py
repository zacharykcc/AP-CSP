# Period 1
# Zachary Wales
# An application that takes in the First, Middle, and Last string a capitlizes them

# Defining Varibles
first = ""
middle = ""
last = ""
done = False

# While until done

while not done:
    # Gets names and checks if done
    first = input("What is the first string? ")
    middle = input("What is the middle string? ")
    last = input("What is the last string? ")

    # Checks for done
    #if first == "done" or :
    #    done = True
    #elif middle == "done":
    #    done = True
    #elif last == "done":
    #    done = True
    if first == "done" or middle == "done" or last == "done" or first == "Done" or middle == "Done" or last == "Done":
        print("Goodbye")
        done = True
    else:  
        first = first.upper()
        middle = middle.upper()
        last = last.upper()

        print(first,middle,last)

input("")
