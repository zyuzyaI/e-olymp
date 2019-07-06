# 060 Площадь многоугольника
from math import fabs as f
n=int(input())
q=input().split()
x,y=int(q[0]),int(q[1])
sum=0
x1=x
y1=y
for i in range(n-1):
    q=input().split()
    x2,y2=int(q[0]),int(q[1])
    sum=sum+(x1+x2)*(y2-y1)
    x1=x2
    y1=y2
sum=f((sum+(x+x2)*(y-y2))/2)
print('%.3f' %sum)
