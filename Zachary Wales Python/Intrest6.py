# Period 1
# Zachary Wales
# An application that calculates and displays compounded interest for an
# investment.

initAmt = float(input("How much would you like to invest? "))
while initAmt <= 0:
    print("Investment must be greater than 0.")
    initAmt = float(input("How much would you like to invest? "))
    
annInt = float(input("What is the annual interest rate? "))
while annInt <= 0 or annInt >= 20:
    print("Investment rate")
# Left off error proofing here

years = int(input("For how long would you like to invest? "))

intrRate0 = annInt/100
intrRate = intrRate0 + 1
finalAmt = float(0)
calcIntrRate = float(0)

print("Year \t\t\t Amount on Deposit")

for count in range(years):
    calcIntrRate = intrRate ** (count+1)
    finalAmt = initAmt*calcIntrRate
    print(str(count+1),"\t\t\t ",round(finalAmt, 2))
