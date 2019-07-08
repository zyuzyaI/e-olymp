# 428 Пушка
q = int(input())
for i in range(q):
	r, x, y = map(int, input().split())
	if (x < 0):
		x = -x
	s = r*x/(2*r - y)
	print('%.2f' %s)
