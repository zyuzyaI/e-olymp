# 696 Банкомат
n = int(input())
for i in range(n):
	a, b, c = map(int, input().split())
	max_k = max(a,b)
	min_k = min(a,b)
	j = c//max_k
	tmp = True
	while j >= 0:
		if (j * max_k) + ((c - j * max_k) // min_k) * min_k == c:
			if a > b:
				print(j, (c - j * max_k) // min_k)
			else:
				print((c - j * max_k) // min_k, j)
			tmp = False
			break
		else:
			j -= 1
	if tmp:
		print('Impossible')
