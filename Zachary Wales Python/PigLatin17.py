# Period 1
# Zachary Wales
# An application that translates either English to Pig Latin or Pig Latin to English

# Get word function
def getWord():
    #Ask “What is your word?”
    word = str(input("What is your word? "))
    #Returns answer
    word = word.strip()
    return word

def EngToPig(myWord):
    print("")
    ##Print title
    print("English to Pig Latin")
    ##Get front of word (1 pt.)
    front = ""
    back = ""
    front1 = myWord[:1]
    front2 = myWord[:2]
    front3 = myWord[:3]
    front = front1
    back = myWord[1:]
    ##If front part of the word is a blend (‘ch’, ‘sh’, ‘th’, ‘wh’, ‘st’ or ‘str’) (3 pt.)
    if front2 == "ch" or front2 == "sh" or front2 == "th" or front2 == "wh" or front2 == "st":
    ##Then the blend is the front
        front = front2
    ##Get the rest of the word (1 pt.)
        back = myWord[2:]
    if front3 == "str":
    ##Then the blend is the front
        front = front3
    ##Get the rest of the word (1 pt.)
        back = myWord[3:]
    ##Return rest of word then space then front with an ‘ay’
    return (myWord+" >>>> "+back+" "+front+"ay")

def PigToEng(myWord):
    #Print Title
    print("")
    print("Pig Latin to English")
    myWord = myWord.strip()
    word = myWord[:-2]
    length = len(word)
    space = word.find(" ")

    back = word[space+1:]
    front = word[:space]

    return (myWord+" >>>> "+(back+front).strip())

##11 pts while menu choice does not equal 3
menuOpt = -1
while menuOpt != 3:
    ##Print title (1 pt.)
    print("-----PIG LATIN TRANSLATOR-----")
    ##Print menu (1 pt.)
    print("Press 1 for English to Pig Latin")
    print("Press 2 for Pig Latin to English")
    print("Press 3 to end!")
    ##Input menu choice (1 pt.)
    menuOpt = int(input("Choice: "))
    ##If menu choice is 1 then (3 pt.)
    if menuOpt == 1:
        ##Get word
        word = getWord()
        ##Call English to Pig Latin function
        print(EngToPig(word))

    ##If menu choice is 2 then (3 pt.)
    if menuOpt == 2:
        ##Get word
        word = getWord()
        ##Call Pig Latin to English function
        print(PigToEng(word))

    ##If menu choice is 3 then (1 pt.)
    if menuOpt == 3:
        ##Print “The End”
        print("The End!")

    ##If menu choice is anything other than 1, 2 or 3 then (1 pt.)
    if menuOpt > 3 or menuOpt < 1:
        ##Print error message
        print("Invalid Choice, Please Choose Again")
