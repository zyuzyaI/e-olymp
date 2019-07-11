# 4739 Решето Эратосфена
a, b = map(int, input().split())
list_erat = [True] * 100001
list_erat[0] = list_erat[1] = False
for i in range(2, 10001):
	for j in range(2 * i, 100001, i):
		list_erat[j] = False
for k in range(a, b+1):
	if list_erat[k]:
		print(k, end=' ')
