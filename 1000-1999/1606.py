# 1606 Сумма первой и последней цифры числа
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

print(c[0]+c[-1])
