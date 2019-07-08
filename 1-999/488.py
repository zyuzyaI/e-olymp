# 488 Обход матрицы "змейкой"
n = int(input())
c = []
k = 0
for i in range(n):
	a = []
	for j in range(n):
		k += 1
		a.append(k)
	c.append(a)
for i in range(n):
    if i % 2 == 1:
        c[i].reverse()
        print(*c[i])
    else:
    	print(*c[i])
