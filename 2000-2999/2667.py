# Змейка №2667 
n, m, x, y = map(int, input().split())
if x % 2:
	print((x - 1)*m + y - 1)
else:
	print((x - 1)*m + (m - y + 1) - 1)


