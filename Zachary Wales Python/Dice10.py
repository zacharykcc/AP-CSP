# Period 1
# Zachary Wales
# An application that will simulate 2 dice being rolled

import random

# Dice pairs
SE = 0
B = 0
BF = 0
SP = 0
PP = 0
BC = 0

numTimes = int(input("How many times would you like to roll 2 dice? "))
print("Count\t\tDie1\t\tDie2\t\tName")
print("----\t\t----\t\t----\t\t----")
# Dice Sim plus printing
for i in range(numTimes):
    extra = ""
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    if die1 == 1 and die2 == 1:
        extra = "Snake Eyes"
        SE = SE+1
    if die1 == 2 and die2 == 2:
        extra = "Ballerina"
        B = B+1
    if die1 == 3 and die2 == 3:
        extra = "Brooklyn Forest"
        BF = BF+1
    if die1 == 4 and die2 == 4:
        extra = "Square Pair"
        SP = SP+1
    if die1 == 5 and die2 == 5:
        extra = "Puppy Paws"
        PP = PP+1
    if die1 == 6 and die2 == 6:
        extra = "Box Cars"
        BC = BC+1
    print(str(i+1)+"\t\t"+str(die1)+"\t\t"+str(die2)+"\t\t"+extra)

#Stats
print("")
print("After",str(numTimes),"rolls, there are:")
print(str(SE)+" pairs of ones. That is "+str(round(100*(SE/numTimes), 1))+"%")
print(str(B)+" pairs of twos. That is "+str(round(100*(B/numTimes), 1))+"%")
print(str(BF)+" pairs of threes. That is "+str(round(100*(BF/numTimes), 1))+"%")
print(str(SP)+" pairs of fours. That is "+str(round(100*(SP/numTimes), 1))+"%")
print(str(PP)+" pairs of fives. That is "+str(round(100*(PP/numTimes), 1))+"%")
print(str(BC)+" pairs of sixes. That is "+str(round(100*(BC/numTimes), 1))+"%")
