# 8934 134
n, m = map(int, input().split())
for i in range(max(n,m), min(n,m)-1, -1):
	print(i, end=' ')
