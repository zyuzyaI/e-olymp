# 7534 Замкнутое сокровище
k = int(input())
for a in range(k):
	n, m = map(int, input().split())
	c = [[1 if j == 0 else 0 for j in range(m+1)] for i in range(n)]
	for i in range(n):
		for j in range(1,m+1):
			c[i][j] = c[i - 1][j] + c[i - 1][j - 1]
	print(c[n-1][m - 1])