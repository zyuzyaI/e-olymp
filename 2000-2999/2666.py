# 2666 Половина
n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i < j:
            a[i][j] =1
        elif i > j:
            a[i][j] = 2
        else:
            a[i][j] = 0
a.reverse()
for row in a:
    print(*row, sep='')
