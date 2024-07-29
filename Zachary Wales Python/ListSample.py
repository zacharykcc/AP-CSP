import random
basket = ["apple","bannana","cherry"]
Fruit = random.choice(basket)
#basket.remove(Fruit)
print(Fruit)
#print(basket)
print("")

for n in range(len(basket)):
    print(basket[n])
print("")

# item could be anything, just prints the whole basket
for item in basket:
    print(item)
print("")

basket.append("durian")
print(basket)
