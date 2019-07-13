# 4760 Сдвиг нулей
n1=int(input())
n=input().split()
c=[]
c1=[]
for i in n:
    if i!='0':
        c.append(i)
    else:
        c1.append(i)
k=c+c1
for i in k:
    print(i, end=' ')
