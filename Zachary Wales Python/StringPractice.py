# a
name = "Zachary Wales"

first = name[:7]


last = name[8:]

#print(last+', '+first)

#for i in range(len(name)):
#    print(name[i])

for i in range(len(name)-1,-1,-1):
    print(name[i], end='')
print("")
