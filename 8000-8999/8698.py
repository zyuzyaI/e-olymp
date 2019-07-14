# 8698 Повторение цифры
outputfile = open('output.txt', 'w')
with open("input.txt") as file:
    k = [j.split() for j in file]
q=1
c=[]
for i in k:
    if i not in c:
        q+=1
        c.append(i)
    else:
        break


outputfile.write(str(q)+'\n')
outputfile.close()
