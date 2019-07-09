# 962 Наибольшая сторона четырёхугольника
import math
n=input().split()
c=[int(i) for i in n]

x=[]
y=[]
for j in range(8):
    if j%2==0:
        x.append((c[j]))
    else:
        y.append((c[j]))
a=[]
for i in range(3,-1,-1):
    k=((x[i]-x[i-1])**2 + (y[i]-y[i-1])**2)**0.5
    a.append(k)
b=max(a)

print('%.2f' %b)
