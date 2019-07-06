# 057 Бабочка-санитар
from math  import sqrt

n=input().split()
x1,y1=int(n[0]),int(n[1])
n=input().split()
x2,y2,z2=int(n[0]),int(n[1]),int(n[2])
S = sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) + z2*z2)
print('%.3f' %(1/S))
