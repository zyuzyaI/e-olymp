# 8241 Функция - 3
from math import sin
def f(x,y):
    c=x**2+sin(x*y)-y*y
    return c
with open("input.txt") as file:
    k = [j.split() for j in file]
outputfile = open('output.txt','w')
for i in k:
    h=('%.4f' %(f(float(i[0]),float(i[1]))))
    outputfile.write(str(h)+'\n')
outputfile.close()
