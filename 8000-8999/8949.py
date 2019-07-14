# 8949 Шаблон 4
n, m = map(int, input().split())
k = 1
for i in range(n):
	for j in range(m):
		print('#', end='')
		k += 1
	print()
