# 2325 Два числа
n=input().split()
v=''.join(n[0]+n[1])
mass=[int(i) for i in v]
mass.sort()
mass.reverse()
for i in range(len(v)):
    print(mass[i], end='')
