# 702 Очень наибольший общий делитель
def f(a, b):
	while a*b != 0:
		if a > b:
			a %= b
		else:
			b %= a
	return a + b

n = int(input())
for i in range(n):
	a = int(input())
	b = int(input())
	print(f(a, b))
