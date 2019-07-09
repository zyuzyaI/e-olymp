# 1623 Чётные и нечётные числа
n=[int(i) for i in (input().split())]
double=0
not_double=0
for i in n:
    if i%2==0:
        double+=1
    else:
        not_double+=1
print('YES' if double>=1 and not_double>=1 else 'NO')
