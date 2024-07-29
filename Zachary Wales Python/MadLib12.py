# Period 1
# Zachary Wales
# Below is some python code for a madlib program.
# You are to cnp this code into a new program. (madlib 12.py)
# Create the appropriate number of lists (look in the code for the proper name of the list).
# Each List will have 5 elements, 
# that will randomly assign an element to the part of the story.  
# The program should not allow a word to be repeated.  
# See the sample output from class.
# Only one portion of the code below should be changed and you will see it "<here>"

import random

def randList(myList):
    myWord = random.choice(myList)
    myList.remove(myWord)
    return myWord
# Lists
adj = ["Clean","Cool","Distinct","Elderly","Elegant"]
noun = ["River","City","Road","Zoo","Farm"]
plNoun = ["Goats","Cows","Mooses","Salmon","Pigs"]
ingVerbs = ["Running","Swimming","Walking","Jumping","Watching"]
bodyParts = ["Ear","Arm","Leg","Eye","Tongue"]
places = ["Ocean","Beach","Hotel","Retirement Home","Disney World"]
games = ["Tag","Hide & Seek","Freeze Tag","Dodgeball","Hockey"]
plants = ["Sunflower","Palm Tree","Rose","Sumac","Oak"]

### Seperate adjectives
##adj1 = random.choice(adj)
##adj.remove(adj1)
##
##adj2 = random.choice(adj)
##adj.remove(adj2)
##
##adj3 = random.choice(adj)
##adj.remove(adj3)
##
### Seperate Nouns
##noun1 = random.choice(noun)
##noun.remove(noun1)
##
##noun2 = random.choice(noun)
##noun.remove(noun2)
##
##noun3 = random.choice(noun)
##noun.remove(noun3)
##
##noun4 = random.choice(noun)
##noun.remove(noun4)
##
### Seperate Plural Nouns
##pluralNoun1 = random.choice(plNoun)
##plNoun.remove(pluralNoun1)
##
##pluralNoun2 = random.choice(plNoun)
##plNoun.remove(pluralNoun2)
##
##pluralNoun3 = random.choice(plNoun)
##plNoun.remove(pluralNoun3)
##
##pluralNoun4 = random.choice(plNoun)
##plNoun.remove(pluralNoun4)
##
### Seperate Ing Verbs
##ingVerb1 = random.choice(ingVerbs)
##ingVerbs.remove(ingVerb1)
##
##ingVerb2 = random.choice(ingVerbs)
##ingVerbs.remove(ingVerb2)
##
##ingVerb3 = random.choice(ingVerbs)
##ingVerbs.remove(ingVerb3)
##
##ingVerb4 = random.choice(ingVerbs)
##ingVerbs.remove(ingVerb4)
##
### Seperate Games
##game1 = random.choice(games)
##games.remove(game1)
##
### Seperate Plants
##plant1 = random.choice(plants)
##plants.remove(plant1)
##
### Seperate Bodyparts
##bodyPart1 = random.choice(bodyParts)
##bodyParts.remove(bodyPart1)
##
### Seperate Places
##place1 = random.choice(places)
##places.remove(place1)

# Printing of Mad Lib

print()
print("-------------My Mad Lib-------------")
print()
print("A vacation is when you take a trip to some " + randList(adj) +" place")
print("with your " + randList(adj) + " family. Usually you go to some place ")
print("that is near a/an " +randList(noun) +" or up on a/an "+ randList(noun))
print("A good vacation place is one where you can ride " + randList(plNoun))
print("or play " + randList(games) +" or go hunting for " + randList(plNoun) + ".  I like ")
print("to spend my time " + randList(ingVerbs) + " or "+randList(ingVerbs) + ".")
print("When parents go on a vacation, they spend their time eating")
print("three " + randList(plNoun) +" a day, and fathers play golf, and mothers ")
print("sit around " + randList(ingVerbs) + ". Last summer, my little brother ")
print("fell in a/an " + randList(noun) + " and got poison " + randList(plants) + " all")
print("over his " + randList(bodyParts) + ".  My family is going to go to (the) ")
print(randList(places) + " , and I will practice "+randList(ingVerbs)+".  Parents")
print("need vacations more than kids because parents are always very ")
print(randList(adj)+" and because they have to work ", random.randint(1,23)) #insert a random integer generator for the appropriate number here
print("hours every day all year making enough " + randList(plNoun) + " to pay " )
print("for the vacation.")
