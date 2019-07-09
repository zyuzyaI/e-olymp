# 941 Разность
n=int(input())
if n<0:
    n=-n
a=n//100

c=n%10
b=(n//10)%10
k1=(a*b*c)-(a+b+c)
print(k1)
