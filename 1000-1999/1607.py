# 1607 Число в обратном порядке
n=(input())
k=len(n)
c=[]
n=int(n)
for i in range(k):
    x=n%10
    n=n//10
    c.append(x)

for i in c:
    print(i, end='')
