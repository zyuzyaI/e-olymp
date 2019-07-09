# 929 Параллелограм
n=input().split()
n.sort()
k1=n.count(n[0])
k2=n.count(n[2])
if k1==k2==2:
    print('YES')
elif k1==4:
    print('YES')
else:
    print('NO')
