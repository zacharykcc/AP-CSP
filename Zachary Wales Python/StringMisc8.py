# Zachary Wales
# Period 1
# An appliation that reads a string inputed by the user and outputs the Original
# string, the length of the string, the string reversed, and the characters 3-7
# in the string

ogString = str(input("Please enter a String: "))

# Original string
print("String: "+ogString)


#Length of String
print("Length of String: "+str(len(ogString)))

#Reversed String
print("The String reversed: ", end="")
for i in range(len(ogString)-1,-1,-1):
    print(ogString[i], end='')
print("")
#3-7 of string
print("The 3rd through 7th characters are: "+ ogString[2:7])
