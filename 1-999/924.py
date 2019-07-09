# 924 Кольцо
import math
n=input().split()
s=float(n[0])
R=float(n[1])
r=math.sqrt(R*R-s/math.pi)
print('%.2f' %r)
