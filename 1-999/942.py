# 942 Диагонали
from math import sqrt
n=input().split()
xa,ya=float(n[0]),float(n[1])
n=input().split()
xb,yb=float(n[0]),float(n[1])
n=input().split()
xc,yc=float(n[0]),float(n[1])
n=input().split()
xd,yd=float(n[0]),float(n[1])
ac=sqrt((xc-xa)**2+(yc-ya)**2)
bd=sqrt((xd-xb)**2+(yd-yb)**2)
x=(xa+xc)/2
y=(ya+yc)/2
print('%.3f %.3f' %(x,y))
print('%.3f %.3f' %(ac,bd))
