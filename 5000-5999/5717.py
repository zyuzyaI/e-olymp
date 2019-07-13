# 5717 Ветреная погода 2
q=int(input())
n=[int(i)  for i in input().split()]
k=list(set(n))
k.sort()
mass=[]
b=0
for i in k:
   b=n.count(i)
   mass.append((i,b))
c=mass[0][0]
c1=mass[0][1]
for i in range(1,len(mass)):
    if c1<mass[i][1]:
        c=mass[i][0]
        c1=mass[i][1]
print(c)
