# 940 Мажорирующий элемент
n=int(input())
c=input().split()
k=dict((x, c.count(x)) for x in set(c) if c.count(x) > n/2)
if k=={}:
    print(-1)
else:
    b=k.popitem()
    print(b[0])
