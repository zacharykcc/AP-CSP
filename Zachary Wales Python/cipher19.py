# Period 1
# Zachary Wales
# An application that will act as a symmetric cipher

text = ""
cipherd = ""
finished = False

while not finished:
    # Inputs the text to be cipherd and resests the cipherd and reversed varibles
    text = str(input("What would you like to encode/decode?(type 'done' to end): "))
    cipherd = ""
    reverse = ""
    print("")
    lowered = text.lower()

    #Checks if the user is finished
    if lowered == "done":
        finished = True
        print("The End!")
    else:
        #Checks whether on not the text is odd or even
        #and adds a space to the end if its odd
        if (len(text)%2) == 1:
            text = str(text)+" "

        # Reverses the text
        for n in range(len(text)-1,-1,-1):
            reverse=reverse+text[n]

        #Swaps letters around and builds the cipherd string
        for n in range(0, len(text),2):
            cipherd = cipherd+reverse[n+1]+reverse[n]

        print(cipherd)
        print("")
