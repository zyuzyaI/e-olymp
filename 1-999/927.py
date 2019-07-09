# 927 Количество игрушек
import math
n=int(input())
c=0
for i in range(n):
    k=input().split()
    a,b=int(k[0]),float(k[1])
    if b<50:
        c+=a
print(c)
