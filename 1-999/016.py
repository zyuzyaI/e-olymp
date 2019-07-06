# 16 Дракон
s,k,a,b=map(int,input().split())
n=0
c=False
if (a*s==b):
    print(s*k)
else:
    while (n < s * k):
        if ((b-s*a)%(n-s*k)==0):
            d=(b-s*a)/(n-s*k)
            if (b - s >= d * n and a > d * k):
                c=True
                break
        n+=1
    print(n if c else '-1')