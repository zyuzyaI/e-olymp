# 847 Змейка
n = int(input())
mass = []
for i in range(n):
	a = []
	for j in range(n):
		a.append(j)
	mass.append(a)
i, j, tmp = 0, 0, 1

for say in range(1, (n*n)+1):
	mass[i][j] = say
	if tmp == 1 and (i == 0 or j == n-1):
		if j == n-1:
			i += 1
		else:
			j += 1
		tmp = -1
	else:
		if tmp == -1 and (i == n-1 or j == 0):
			if i == n -1:
				j += 1
			else:
				i += 1
			tmp = 1
		else:
			i -= tmp
			j += tmp



for k in range(n):
	for b in range(n):
		print(mass[k][b], end='')
		if b < n - 1:
			print(' ', end='')
	print()
