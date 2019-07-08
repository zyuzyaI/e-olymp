# 497 Лентяй
n = int(input())
for i in range(n):
	m = int(input())
	low = []
	hight = []
	for j in range(m):
		k, q = map(int, input().split())
		low.append(k)
		hight.append(q)
	if max(low) <= min(hight):
		print('YES')
	else:
		print('NO')
