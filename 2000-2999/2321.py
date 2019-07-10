# 2321 Сортировка
n=int(input())
mass=[int(i) for i in (input().split())]
for i in range(n):
    k=i
    while k>0 and mass[k-1]>mass[k]:
        mass[k],mass[k-1]=mass[k-1],mass[k]
        k-=1
for i in range(n):
    print(mass[i], end=' ')
