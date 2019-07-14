# 8626 Две цифры подряд
n=int(input())
a=n//1000
b=(n//100)%10
c=(n//10)%10
d=n%10
k=0
if a==3:
    if b==7:
        k=1
if b==3:
    if c==7:
        k=1
if c==3:
    if d==7:
        k=1
if k==1:
    print('YES')
else:
    print("NO")
