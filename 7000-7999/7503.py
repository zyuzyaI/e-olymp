# 7503 Олимпиада
n,m=map(int,input().split())
s=0
p=0
q=[int(i) for i in input().split()]
for i in q:
    s+=i
    if i>p:
        p=i
res=(s+m-1)//m
if res < p:
    res = p
print(res)
