# 513 Проблема Николая
n , m = map(int, input().split())
k = 1
if ( n >= m):
	print(0)
else:
	for i in range(2, n+1):
		k = (k * i ) % m
	print(k)
