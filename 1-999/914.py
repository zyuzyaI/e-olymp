# 914 Модуль максимального
n=int(input())
n1=input().split()
c=[]

for i in n1:
    i=float(i)
    if i<0:
        i=-i
        c.append(i)
    else:
        c.append(i)

print('%.2f' %(max(c)))
