# 1151 Кладоискатель
a, b = map(int, input().split())
def gcd(a, b):
	while a*b != 0:
		if a > b:
			a %= b
		else:
			b %= a
	return a + b
print(gcd(a,b))
