# 1000 Задача a + b
outputfile = open('output.txt', 'w')
with open("input.txt") as file:
    k = [j.split() for j in file]

for i in k:
    b=int(i[0])+int(i[1])
    outputfile.write(str(b)+'\n')
outputfile.close()
