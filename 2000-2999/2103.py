# 2103 Рюкзак
q=input().split()
w,n=int(q[0]),int(q[1])
mass=[int(i) for i in input().split()]
if w<n:
    mass.sort()
    mass=mass[::-1]
    c=sum(mass[:w])

else:
    c=sum(mass)
print(c)
