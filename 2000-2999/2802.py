# 2802 Битовое представление
with open("input.txt") as file:
    k = [j for j in file]
outputfile = open('output.txt','w')
for i in k:
    c=(bin(int(i)))
    outputfile.write(str(c[2:])+'\n')
outputfile.close()
