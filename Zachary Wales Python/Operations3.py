# Zachary Wales
# Period 1
# A program that askes the user for the input of two numbers.
# The program will then display the 5 computational operations
# The output will then be the mathematical equations of the 2 numbers performing the operations.

numberOne = input("What is the first number? ")
numberTwo = input("What is the second number? ")

addition = int(numberOne) + int(numberTwo)
subtraction = int(numberOne) - int(numberTwo)
multiplication = int(numberOne) * int(numberTwo)
division = int(numberOne) / int(numberTwo)
modulus = int(numberOne) % int(numberTwo)

print("")
print(str(numberOne)+" + "+str(numberTwo)+" = "+str(addition))
print(str(numberOne)+" - "+str(numberTwo)+" = "+str(subtraction))
print(str(numberOne)+" x "+str(numberTwo)+" = "+str(multiplication))
print(str(numberOne)+" ÷ "+str(numberTwo)+" = "+str(division))
print(str(numberOne)+" mod "+str(numberTwo)+" = "+str(modulus))
