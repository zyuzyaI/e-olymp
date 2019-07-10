# 2130 Угол между векторами
import math
n=input().split()
x1=int(n[0])
y1=int(n[1])
x2=int(n[2])
y2=int(n[3])
a=math.acos(((x1*x2)+(y1*y2))/((x1**2+y1**2)**0.5*(x2**2+y2**2)**0.5))
print('%.5f' %a)
