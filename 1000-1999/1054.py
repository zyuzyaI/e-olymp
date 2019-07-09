# 1054 Счастливое число Тигры
def f(a):
	c = 0
	if len(a) == 1:
		if a == '1' or a == '7':
			return 1
		return 0
	for i in a:
		c += int(i)**2
	a = str(c)
	return f(a)


n = int(input())
mass = input().split()
for i in mass:
	print(f(i), end='')
