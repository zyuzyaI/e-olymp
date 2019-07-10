# 2619 Счастливый билетик 2
n=int(input())
massive=[int(i) for i in input().split()]
cem=0

for i in range(n):
    cem=cem+massive[i]
if (cem%2 == 0):
    solCem=0
    for k in range(n):
        cem=cem-massive[k]
        solCem=solCem+massive[k]
        if cem==solCem:
            print(k + 1)
            break
        elif cem<solCem:
            print(-1)
            break
else:
    print(-1)
