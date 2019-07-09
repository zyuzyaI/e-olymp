# 1213 Массивные числа
n=(input().split())
c1=(n[0])
c2=(n[1])
c1=c1.split('^')
c2=c2.split('^')
k1=(int(c1[0])**int(c1[1]))
k2=(int(c2[0])**int(c2[1]))
if k1>k2:
    print(n[0])
else:
    print(n[1])
