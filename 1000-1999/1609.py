# 1609 Количество заданных цифр в числе
n=(input())
k=len(n)
c=[]
n=int(n)
if n<0:
    n=-n
    k=k-1
for i in range(k):
    x=n%10
    n=n//10
    c.append(x)

a=int(input())
m=c.count(a)
print(m)
