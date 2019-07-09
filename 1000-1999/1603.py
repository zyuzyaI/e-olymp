# 1603 Сумма цифр числа
n=input()
c=len(n)
n=int(n)
if n<0:
    n=-n
    c=c-1
q=[]
for i in range(c):
    k=n%10
    n=n//10
    q.append(k)
print(sum(q))
