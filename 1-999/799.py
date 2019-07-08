# 799 Покупка билетов
q=int(input())
c=[0]
a=[0]
b=[0]
for i in range(q):
    w=[int(j) for j in input().split()]

    c.append(w[2])
    a.append(w[0])
    b.append(w[1])
if q<2:
    print(min(a[1],b[1],c[1]))
else:
    t=[0,a[1],min(a[1]+a[2],b[1])]+[0]*(q-2)
    for i in range(3,q+1):
        t[i]=min(t[i-1]+a[i],t[i-2]+b[i-1],t[i-3]+c[i-2])
    print(t[-1])
