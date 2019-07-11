# 2665 Экспедиция
q=[int(i) for i in input().split()]
mass=[]
for i in range(q[0]):
    n=[int(j) for j in input().split()]
    mass.append(n)
c=int(input())
memb=[int(i) for i in input().split()]
our_mass=[]
for i in range(q[0]):
    our_mass+=mass[i]
our_mass.sort()
memb.sort()
k=0
c=0
for j in range(len(our_mass)):
    while c<len(our_mass):
        if our_mass[c]>=memb[j]:
            k+=1
            c+=1
            break
        c+=1

print(k)
