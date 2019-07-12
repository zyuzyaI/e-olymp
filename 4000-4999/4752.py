# 4752 Кинотеатр
n1=input().split()
n=int(n1[0])
m=int(n1[1])
k=n*m
c=[]
for i in range(n):
    c1=[]
    for j in range(m):
        c1.append(k)
        k-=1
    c1.reverse()
    c.append(c1)
b=[]
for i in range(n):
    b1=[]
    w=n*m-i
    for j in range(m):
        b1.append(w)
        w-=n
    b1.reverse()
    b.append(b1)

r=0
for i in range(n):
    for j in range(m):
        if c[i][j]==b[i][j]:
            r+=1
print(r)
