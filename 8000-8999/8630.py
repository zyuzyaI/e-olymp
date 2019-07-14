# 8630 Максимальная цифра в числе
n=input()
k2=len(n)
c=[]
n=int(n)
for i in range(k2):
    k1=n%10
    n=n//10
    c.append(k1)
a=max(c)

print(a)
