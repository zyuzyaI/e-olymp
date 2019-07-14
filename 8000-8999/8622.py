# 8622 Квадрат максимального
n=input()
k2=len(n)
c=[]
c1=[]
n=int(n)
for i in range(k2):
    k1=n%10
    n=n//10
    c.append(k1)
c.sort()
c.reverse()
a=('%d%d%d' %(c[0], c[1], c[2]))
a=int(a)
print(a**2)
