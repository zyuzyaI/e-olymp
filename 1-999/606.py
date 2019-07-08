# 606 Табло
n = int(input())

tmp = 0
k = 0

for i in range(n+1, 10000):
	k = str(i-1)
	i = str(i)
	for j in range(4):
		if k[j] != i[j]:
			tmp += 1
print(tmp)
