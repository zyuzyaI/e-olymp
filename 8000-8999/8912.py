# 8912 112
k = 0
c = 0
while True:
	i = int(input())
	if i == 0:
		break
	if i < 0:
		k += 1
	else:
		c += i
print(c)
