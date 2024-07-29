#Countious run

string1 = ""
done = False
while not done:
    string1 = input("What is the name? ")
    if string1 == "Banana":
        print("Hooray!")
    elif string1 == "Finish":
        print("Thank your for playing")
        done = True
    else:
        front = string1[0:0]
        back = string1[1:0]
        front = front.upper()
        print(front+back)
        
