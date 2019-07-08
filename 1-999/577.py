# 577 Книга
def f(x):
	if (x < 10):
		return 1
	if (x < 100):
		return 2
	if (x < 1000):
		return 3
	return 4
n = int(input())
seh = 3
while (n > 0):
	seh += 1
	n = n - f(seh)
print(seh)
