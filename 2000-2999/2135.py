# 2135 Положение точек вне прямой
n=input().split()
x1=int(n[0])
y1=int(n[1])
x2=int(n[2])
y2=int(n[3])
a=int(n[4])
b=int(n[5])
c=int(n[6])
a1=a*x1+b*y1+c
a2=a*x2+b*y2+c
if a1<0 and a2<0:
    print('YES')
elif a1>0 and a2>0:
        print('YES')
else:
    print('NO')
