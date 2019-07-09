# 1214 Мультифакториал
n1=input().split()
n=int(n1[0])
k=int(n1[1])
res=1
while n>0:

    res*=n
    if res>10**18:
        res=('overflow')
        break
    n-=k
print(res)
