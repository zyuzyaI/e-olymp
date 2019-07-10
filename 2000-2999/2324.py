# 2324 Разброс
c=int(input())
mass=[int(i) for i in (input().split())]
mass.sort()
for i in mass:
    print(i, end=' ')
