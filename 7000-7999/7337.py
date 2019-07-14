# 7337 Знижки
x=input().split()
a=int(x[0])
b=int(x[1])
n=int(x[2])
if a>=b and a>=n:
    if b>=n:
        q=a+n
    else:
        q=a+b
if b>=a and b>=n:
    if a>=n:
        q=b+n
    else:
        q=b+a
if n>=a and n>=b:
    if a>=b:
        q=n+b
    else:
        q=n+a
print(q)
