# 1952 Контроперация
n=input().split()
n.remove(n[0])
c=[int(i) for i in n ]
k=max(c)
m=min(c)
for i in c:
    if i==k:
        i=m
    print(i, end=' ')
