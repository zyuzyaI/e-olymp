# 2133 Принадлежность точки лучу
n=input().split()
x=float(n[0])
y=float(n[1])
x1=float(n[2])
y1=float(n[3])
x2=float(n[4])
y2=float(n[5])
if (x-x1)*(y2-y1)==(x2-x1)*(y-y1) and (x-x1)*(x2-x1)>=0 and (y-y1)*(y2-y1)>=0:
    print('YES')
else:
    print('NO')
