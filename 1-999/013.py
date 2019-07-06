# 13 Паук и муха
from math import sqrt
def f(x1,y1,x2,y2):
    
    s=sqrt((x1-x2)**2+(y1-y2)**2)
    return s
n=input().split()
a,b,c=int(n[0]),int(n[1]),int(n[2])
q=input().split()
x1,y1,x2,y2,z2=int(q[0]),int(q[1]),int(q[2]),int(q[3]),int(q[4])
if z2==0:
    r=f(x1, y1, x2, y2)
elif x2==0:
    if y2==b:
        if x1+y1<b:
            r=f(x1, y1, -z2, y2)
    r=f(x1, y1, -z2, y2)
    
elif x2==a:
    r=f(x1, y1, a+z2, y2)
elif x2==b:
    r=f(x1, y1, b+z2, y2)
elif y2==0:
    r=f(x1, y1, x2, -z2)
elif (y2==b) and (x2!=0):
    r=f(x1, y1, x2, b+z2)
elif y2==a:
    r=f(x1, y1, x2, a+z2)
print('%.2f' %r)