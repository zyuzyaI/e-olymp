# 5057  Спиралька
n = int(input())
k = 1
m = 0
mass = [[0]*n for i in range(n)]
mass[n//2][n//2] = n*n
for i in range(n//2):

	for j in range(n-m):
		mass[i][j+i] = k
		k += 1

	for j in range(i+1, n-i):
		mass[j][-i-1] = k
		k += 1

	for j in range(i+1, n-i):
		mass[-i-1][-j-1] = k
		k += 1

	for j in range(i+1, n-(i+1)):
		mass[-j-1][i] = k
		k += 1

	m += 2

for i in mass:
    print(*i)
