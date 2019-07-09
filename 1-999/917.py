# 917 Удвоенный минимальный
n=int(input())
n1=input().split()
c=[]
for i in n1:
    i=float(i)
    c.append(i)

k=2*min(c)

print('%.2f' %(k))
