# 478 Белые кубики
n=input().split()
a,b,c=int(n[0]),int(n[1]),int(n[2])
v=(a*b*c)
s=v*6-2*(a*b+b*c+c*a)
print(v, s)
