# 395 "Простые" числа
n = int(input())
s = [int(i) for i in input().split()]
k = []
for i in s:
	c=True
	for j in s:
		if j != i and i % j == 0:
			c=False
	if c :
		k.append(i)
print(*k)
