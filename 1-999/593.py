# 593 Шахматная модель
n, m = map(int, input().split())
mass = []

for i in range(n):

	tmp_mass = []
	for j in range(m):

		if ((i + j) % 2) != n % 2:
			tmp_mass.append('.')
		else:
			tmp_mass.append('X')

	mass.append(tmp_mass)

for i in mass:
	print(*i, sep='')
