# 2391 Стоимость разговора
import math

n=input().split()
a,b,m=int(n[0]),int(n[1]),int(n[2])
if m==0:
    print(0)
else:
    pay=a+b*(math.ceil(m/60))
    print(pay)
