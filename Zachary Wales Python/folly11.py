# Period 1
# Zachary Wales
# A program that demonstrates the futility of playing Luck Sevens>

import random

# Initial stuff
print("*** Welcome to Lucky Seven Dice Game! ***")
print("If the sum of the Dice is 7, you win $4. Otherwise, you lose $1.")
print("")
money = int(input("How much money do you have? "))
numRolls = 0
highMon = money
highRoll = numRolls

# Main
while money > 0:
    numRolls = numRolls + 1
    print("")
    print("--------------------------------")
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    print("Roll# "+str(numRolls)+"   Die 1: "+str(die1)+"\tDie 2: "+str(die2))
    total = die1+die2
    if total == 7:
        money = money + 4
    else:
        money = money - 1
    print("")
    print("You have $"+str(money)+".")
    if money > highMon:
        highMon = money
        highRoll = numRolls

# After no more money
print("You are broke after "+str(numRolls)+" rolls.")
print("You should have quit after "+str(highRoll)+" rolls when you had $"+str(highMon))

