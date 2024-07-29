# Zachary Wales
# Period 1
# An application that reads the input of five integers and determines and
# prints the largest , the smallest and the mean of the group.
# Due: 10/6/2022

firstNum = int(input("Please enter in first number: "))
secondNum = int(input("Please enter in second number: "))
thirdNum = int(input("Please enter in third number: "))
fourthNum = int(input("Please enter in fourth number: "))
fifthNum = int(input("Please enter in fifth number: "))

sum = firstNum + secondNum + thirdNum + fourthNum + fifthNum
mean = sum / 5

# Largest Numbers

if firstNum>secondNum:
    if firstNum>thirdNum:
        if firstNum>fourthNum:
            if firstNum>fifthNum:
                print("The largest number is:",str(firstNum))

if secondNum>firstNum:
    if secondNum>thirdNum:
        if secondNum>fourthNum:
            if secondNum>fifthNum:
                print("The largest number is:",str(secondNum))

if thirdNum>secondNum:
    if thirdNum>firstNum:
        if thirdNum>fourthNum:
            if thirdNum>fifthNum:
                print("The largest number is:",str(thirdNum))

if fourthNum>secondNum:
    if fourthNum>thirdNum:
        if fourthNum>firstNum:
            if fourthNum>fifthNum:
                print("The largest number is:",str(fourthNum))
if fifthNum>secondNum:
    if fifthNum>thirdNum:
        if fifthNum>fourthNum:
            if fifthNum>firstNum:
                print("The largest number is:",str(fifthNum))


#Smallest Numbers


if firstNum<secondNum:
    if firstNum<thirdNum:
        if firstNum<fourthNum:
            if firstNum<fifthNum:
                print("The smallest number is:",str(firstNum))

if secondNum<firstNum:
    if secondNum<thirdNum:
        if secondNum<fourthNum:
            if secondNum<fifthNum:
                print("The smallest number is:",str(secondNum))

if thirdNum<secondNum:
    if thirdNum<firstNum:
        if thirdNum<fourthNum:
            if thirdNum<fifthNum:
                print("The smallest number is:",str(thirdNum))

if fourthNum<secondNum:
    if fourthNum<thirdNum:
        if fourthNum<firstNum:
            if fourthNum<fifthNum:
                print("The smallest number is:",str(fourthNum))
if fifthNum<secondNum:
    if fifthNum<thirdNum:
        if fifthNum<fourthNum:
            if fifthNum<firstNum:
                print("The smallest number is:",str(fifthNum))

# If they are all the same value
if firstNum == secondNum:
    if firstNum == thirdNum:
        if firstNum == fourthNum:
            if firstNum == fifthNum:
                print("The largest number is:",str(firstNum))
                print("The smallest number is:",str(firstNum))
#Mean Print
print("The mean of the 5 numbers is:",mean,)
