# 904 Увеличить на 2
n=int(input())
n1=input().split()
c=[]
for i in n1:
    i=int(i)
    if i>=0:
        i=i+2
        c.append(i)
    else:
        c.append(i)
for j in c:
    print(j, end=' ')
