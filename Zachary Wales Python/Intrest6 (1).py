# Period 1
# Zachary Wales
# An application that calculates and displays compounded interest for an
# investment.

# Gets user input and checks it
initAmt = float(input("How much would you like to invest? "))
while initAmt <= 0:
    print("")
    print("Investment must be greater than 0.")
    initAmt = float(input("How much would you like to invest? "))
    
annInt = float(input("What is the annual interest rate? "))
while annInt <= 0 or annInt > 20:
    print("")
    print("Investment rate must be greater than 0 and less than 20%.")
    annInt = float(input("What is the annual interest rate? "))

years = int(input("For how long would you like to invest? "))
while initAmt <= 0:
    print("")
    print("Years must be greater than 0.")
    years = int(input("For how long would you like to invest? "))

#Math
annInt = annInt / 100
finAmt = float(0)

# Sets up format
print("Year \t\t\t Amount on Deposit")

# Does more math and formats
for count in range(years):
    count += 1
    finAmt = initAmt*annInt*count
    finAmt += initAmt
    print(count,"\t\t\t ",str(finAmt))
