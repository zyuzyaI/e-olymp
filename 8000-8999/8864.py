# 8864 064
n, m = map(int, input().split())

if abs(n) == n and abs(m) == m:
	print(1)
elif n < 0 and m < 0:
	print(1)
else:
	print(0)
