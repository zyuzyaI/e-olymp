# 988 Подпоследовательности
n = int(input())
mass = [int(i) for i in input().split()]
d = [1] * n

for i in range(n):

	for j in range(i):
		if mass[j] < mass[i]:
			d[i] = max(d[i], d[j] + 1)


print(max(d))
