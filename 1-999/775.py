# 775 Подготовка
k, m, n = map(int, input().split())
mass = [int(i) for i in input().split()]
mass.sort()
n_m = m*n
tmp = 0
suma = 0
for i in  mass[::-1]:
	suma += 1
	tmp += i
	if tmp >= n_m:
		print(suma)
		break
