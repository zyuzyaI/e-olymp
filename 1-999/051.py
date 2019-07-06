# 051 Стоимость K-домино
s=int(input())
if s==0:
    print(0)
else:
    t=1
    k=0
    while s>t:
        k+=1
        t+=k+1
    if s>=k:
        k+=1
    print(k)
