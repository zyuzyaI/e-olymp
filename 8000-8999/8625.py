# 8625 Удалить цифру
n=int(input())
a=n//100
b=(n//10)%10
c=n%10
q=()
k=min(a,b,c)
if k==a:
    q=(b,c)
    k=0
if k==b:
    q=(a,c)
if k==c:
    q=(a,b)
print(str(q[0])+str(q[1]))
