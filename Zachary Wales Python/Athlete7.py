# Period 1
# Zachary Wales
# An application that will calculate an athlete’s target heart rate.

#Inputs
name = input("What is the athlete's name? ")
year = int(input("What year was "+name+" born? "))
age = 2022 - year

# Checks
while age < 13:
    age = 2022 - year
    print(str(age)+" is too young")
    print("Age needs to be 13 and older")
    year = int(input("What year was "+name+" born? "))
    age = 2022 - year

while age > 219:
    age = 2022 - year
    print(str(age)+" is too old")
    print("Age needs to be younger than 219")
    year = int(input("What year was "+name+" born? "))
    age = 2022 - year

# Calculations
maxHeartRate = 220-age
minTarget = round(maxHeartRate*.50, 2)
maxTarget = round(maxHeartRate*.85, 2)

# Outputs
print(name,"is ",str(age),"years old.")
print("Minimum target heart rate is "+str(minTarget))
print("Maximum target heart rate is "+str(maxTarget))
