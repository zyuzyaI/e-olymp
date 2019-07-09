# 934 Высоты треугольника
import math
n=input().split()
a=int(n[0])
b=int(n[1])
c=int(n[2])
p=(a+b+c)/2
s=math.sqrt(p*(p-a)*(p-b)*(p-c))

Ha=(2/a)*s

Hb=(2/b)*s
Hc=(2/c)*s
print('%.2f %.2f %.2f' %(Ha, Hb, Hc))
