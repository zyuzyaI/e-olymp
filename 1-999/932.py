# 932 Высота треугольника
n=input().split()
s=int(n[0])
a=int(n[1])
h1=(-a+(a*a+8*s)**0.5)/2
h2=(-a-(a*a+8*s)**0.5)/2
h=h1 if h1>0 else h2
print('%.2f' %h)
