# Period 1
# Zachary Wales
# An application that simulates a player vs. computer game of Rock,
# Paper, Scissors (best of 5).

#Imports random
import random

#Varibles
computerOptions = ["r", "p", "s"]
finished = False
games = 0
pScore = 0
cScore = 0

#Gets players name and start screen
userName = str(input("Please enter your name: "))
print("Welcome to Rock, Paper, Scissors( "+ userName + " vs. Computer )")
print("")
print("")

# The main alogirithm
while not finished:
    # Sequences games
    games = games + 1

    # Makes sure that the game should still be running
    if pScore >= 3 or cScore >= 3 or games == 6:
        finished = True

    # Double Check to make sure the game should be running
    if finished == False:
        # Game menu screen and user input
        print("-------------------Game "+str(games)+"---------------------")
        pOption = input("Please choose Rock(R), Paper(P), or Scissors(S): ").lower()

    # Checks to make sure there is a good input for the user's choice
        while pOption != "p" and pOption != "s" and pOption != "r":
            print("")
            print("")
            print("Invalid Choice, Please choose Rock(R), Paper(P), or Scissors(S):")
            pOption = input("Please choose Rock(R), Paper(P), or Scissors(S): ").lower()

        cOption = random.choice(computerOptions)

    #Outputs the selections from the computer and the player
        if pOption == "p":
            print(userName + " chose Paper.")
        elif pOption == "r":
            print(userName + " chose Rock.")
        elif pOption == "s":
            print(userName + " chose Scissors.")

        if cOption == "p":
            print("Computer Chose Paper.")
        elif cOption == "r":
            print("Computer Chose Rock.")
        elif cOption == "s":
            print("Computer Chose Scissors.")

        # An abstraction to find out who won/lost/tied
        if cOption == pOption:
            games = games - 1
            print("Tie")
        elif cOption == "r" and pOption == "s":
            cScore = cScore + 1
            print("Computer Wins!")
        elif cOption == "s" and pOption == "p":
            cScore = cScore + 1
            print("Computer Wins!")
        elif cOption == "p" and pOption == "r":
            cScore = cScore + 1
            print("Computer Wins")
        else:
            print(userName +" Wins!")
            pScore = pScore + 1
        # End of the abstraction
        
        print("")
        print("")
# End of the algorithm


#Prints who wins
print("===End of Game===")
if pScore == 3:
    print(userName + " wins")

if cScore == 3:
    print("Computer wins")

print(userName + " " + str(pScore))
print("Computer "+str(cScore))
