# 2132 Принадлежность точки прямой
n=input().split()
x=int(n[0])
y=int(n[1])
a=int(n[2])
b=int(n[3])
c=int(n[4])
if a*x+b*y+c==0:
    print('YES')
else:
    print('NO')
