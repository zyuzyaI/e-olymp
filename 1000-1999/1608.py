# 1608 Число-палиндром
n=(input())
k=len(n)
n=int(n)
c=[]

for i in range(k):
    m=n%10
    n=n//10
    c.append(m)
c1=c[::-1]
if c1==c:
    print('Yes')
else:
    print('No')
