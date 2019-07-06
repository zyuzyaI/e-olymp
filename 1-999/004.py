import math
n=input().split(' ')
x1=float(n[0])
y1=float(n[1])
r1=float(n[2])
x2=float(n[3])
y2=float(n[4])
r2=float(n[5])
k=0
if x1==x2 and y1==y2:
    if r1==r2:
        k=-1
    else:
        k=0
else:
    d=math.sqrt((x1-x2)**2+(y1-y2)**2)
  
    if d==(r1+r2) or d==math.fabs(r1-r2):
        k=1
    else:
        if d>(r1+r2) or d+r2<r1 :
            k=0
        else:
            k=2

        
    
print(k)