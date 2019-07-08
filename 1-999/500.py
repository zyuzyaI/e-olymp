# 500 Ремонт
import math
n=int(input())
for i in range(n):
    k=input().split()
    a,b,h=int(k[0]),int(k[1]),int(k[2])
    c=2*a*h+2*b*h
    print(math.ceil(c/16))
