# 027 Циклические сдвиги
n=int(input())
k=bin(n)
c=0
d=str(k[2:])
for i in range(len(d)):
    d=d[1:]+d[0]
    if c<sum(int(c)*(2**i) for i, c in enumerate(d[::-1])):
        c=sum(int(c)*(2**i) for i, c in enumerate(d[::-1]))
print(c)