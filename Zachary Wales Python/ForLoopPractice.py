# Practice For loops

# 1,3,6,10,15,21,28

triNum = int(input("How many triangular numbers would you like? "))
counter = 4
total = 0

for n in range(1, triNum+1):
    total += n  # <--- Better than total = total + n
    print(total,end="")
    if n < triNum:
        print(", ", end="")
    else:
        print(".", end="")
