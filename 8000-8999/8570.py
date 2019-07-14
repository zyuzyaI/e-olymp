# 8570 Длина слов
spis=[]
with open("input.txt") as file:
    k = [j.split() for j in file]
for j in k:
    for i in j:
        h=len(i)
        spis.append(h)

outputfile = open('output.txt','w')
for j in spis:
    outputfile.write(str(j)+' ')
outputfile.close()
