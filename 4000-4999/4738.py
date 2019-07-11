# 4738 Сортировка
n=int(input())
n1=input().split()
c=[]
for i in n1:
    c.append(int(i))
c.sort()
c=c[::-1]
for j in c:
    print(j, end=' ')
