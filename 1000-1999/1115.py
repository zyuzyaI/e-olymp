# 1115 Отношение площадей
from math  import sqrt
def f(x1,y1,z1,x2,y2,z2):
    a=sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
    return a
n=[int(i) for i in (input().split())]
x1, y1, z1, x2, y2, z2, x3, y3, z3=n[0],n[1],n[2],n[3],n[4],n[5],n[6],n[7],n[8]
a=f(x1, y1, z1, x2, y2, z2)
b=f(x2, y2, z2, x3, y3, z3)
c=f(x3, y3, z3, x1, y1, z1)

v=('%.3f' %((((a+c-b)*(a+b-c)*(b+c-a))/(2*a*b*c))**2))
if float(v)<0.001:
    print('Zero!')
else:
    print(v)
