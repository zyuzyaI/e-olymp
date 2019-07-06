# 076 Нова шафа
n=input().split()
a=float(n[0])
b=float(n[1])
x=float(n[2])
y=float(n[3])
z=float(n[4])
k=0
if (a>x and b>y) or (a>y and b>x) or (a>y and b>z)or (a>z and b>y) or (a>x and b>z) or (a>z and b>x):
    k=1


print(k)
