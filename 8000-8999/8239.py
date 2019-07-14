# 8239  Функция - 1
with open("input.txt") as file:
    k = [float(j) for j in file]
outputfile = open('output.txt','w')
for i in k:
    h=('%.4f' %(i**3+2*i**2-3))
    outputfile.write(str(h)+'\n')
outputfile.close()
