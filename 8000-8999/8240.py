# 8240 Функция - 2
from math import sin
def f(x):
    c=x**0.5+2*x+sin(x)
    return c
with open("input.txt") as file:
    k = [float(j) for j in file]
outputfile = open('output.txt','w')
for i in k:
    h=('%.4f' %(f(i)))
    outputfile.write(str(h)+'\n')
outputfile.close()
