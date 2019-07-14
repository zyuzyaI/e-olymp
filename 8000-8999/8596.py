# 8596 Путешествие с запада на восток
n=input().split()
x,a,b=int(n[0]),int(n[1]),int(n[2])
n1=input().split()
c=[int(i) for i in n1]
c.reverse()
k=0
for j in range(1,x):
    if (c[j-1]-c[j])*a<b:
        k+=(c[j-1]-c[j])*a
    else:
        k+=b
print(k)
