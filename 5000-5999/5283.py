# 5283 Оттепель
n=int(input())
k=0
v=[]
mass=input().split()
for i in mass:
    i=int(i)
    if i>0:
        k+=1
    if i<=0:
        v.append(k)
        k=0
    v.append(k)
print(max(v))
