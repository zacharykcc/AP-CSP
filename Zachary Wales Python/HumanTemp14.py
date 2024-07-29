# Period 1
# Zachary Wales
# An application called 'HumanTemp14' that will help a person decide what medical treatment they should seek based on their temperature.

# Converts from fahrenheit to celcius
# F = 9/5C + 32
# C = 5/9(F-32)
# Round Temps to a single decimal place

done = False
done2 = False
finished = False



while not finished:
# Patient Input of Temp
    fTemp = float(input("What is the patient's temperature (in Fahrenheit)? "))

    # 7 Outcomes
    if fTemp < 90 or fTemp > 105:
        print("")
        print("")
        print("**********************************************************")
        print("***Take the patient to the Emergency Room Immediately!!***")
        print("**********************************************************")
        print("")
        print("")
    elif fTemp >= 90 and fTemp < 95:
        print("The patient potentially has hypothermia!")
        print("Cover with Blankets.")
        print("Monitor Breathing. Provide warm Beverages!")
    elif fTemp >= 95 and fTemp < 97.7 or fTemp >= 99.5 and fTemp < 100.9:
        print("Observe Patient!")
    elif fTemp >= 97.7 and fTemp < 99.5:
        print("The patient is in the normal range of temperature.")
    elif fTemp >= 100.9 and fTemp < 105:
        print("The patient has a fever!")
        print("Rest and drink plenty of fluids. Medication isn't needed.")
        print("Call the doctor if the fever is accompanied by a severe headache, stiff neck,")
        print("shortness of breath, or other unusual signs or symptoms.")

#Patient Output of Temp
    print("")
    cTemp = float((5/9)*(fTemp-32))
    print("The patient's temperature in Cel is "+str(round(cTemp,1))+" C")

#If the person is done using the program
    # Done is yes/no
    # Done2 true/false for the 2nd while loop
    # Finished is if the program is completley finished

    done = input("Type yes to continue ")
    while not done2:
        if done == "Yes" or done == "y" or done == "Y" or done == "YES" or done == "yes":
            finished = False
            done2 = True
            print("")
            print("")
        elif done == "No" or done == "n" or done == "N" or done == "NO" or done == "no":
            finished = True
            done2 = True
        else:
            print("Response Invalid")
            print("For Yes respond with Yes, y, yes, Y, or YES")
            print("For No respond with No, n, no, N, or NO")
            done = input("Type yes to continue ")
    done2 = False

print("The End")
