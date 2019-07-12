# 4748 Бонусный уровень
n = int(input())

tmp = 0
mass = [[0 for i in range(n)] for j in range(n)]
mass[0][0] = 1
if n > 1:
	mass[1][0] = 2
x = 1
y = 0
for i in range(3, n*n + 1):
	if tmp % 2 == 0:
		if (x != 0 and y != n - 1):
			x -= 1
			y += 1
		elif (x == 0 and y == n - 1):
			x += 1
			tmp += 1
		elif (x == 0):
			y += 1
			tmp += 1
		elif (y == n - 1):
			x += 1
			tmp += 1
	else:
		if (x != n - 1 and y != 0):
			x += 1
			y -= 1
		elif (x == n - 1 and y == 0):
			y += 1
			tmp += 1
		elif (x == n - 1):
			y += 1
			tmp += 1
		elif (y == 0):
			x += 1
			tmp += 1
	mass[x][y] = i;

for i in range(n):
	print(*mass[i])
