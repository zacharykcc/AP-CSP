# Period 1
# Zachary Wales
# An application that rolls 2 dice 20 times

import random

print("Roll\t\tDie 1\t\tDie 2")
for count in range(20):
    roll = count + 1
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    print(""+str(roll)+"\t\t"+str(die1)+"\t\t"+str(die2))
