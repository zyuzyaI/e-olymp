# 136 Відрізок
def count_dis(a,b):
	while a*b != 0:
		if a > b:
			a %= b
		else:
			b  %= a
	return a + b
x1, y1, x2, y2 = map(int, input().split())
x = abs(x1 - x2)
y = abs(y1 - y2)
print(count_dis(x, y) + 1)
