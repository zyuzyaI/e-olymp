# 4750 Заполнение
n=int(input())
k=1

c=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append(k)
        k+=1
    c.append(a)
c1=[]

for i in range(n):
    c2=[]
    if i%2==0:
        c1.append(c[i])
    else:
        for j in c[i]:
            c2.append(j)
        c2.reverse()
        c1.append(c2)


for i in range(n):
    for j in range(n):
        print(c1[i][j], end=' ')
    print()
