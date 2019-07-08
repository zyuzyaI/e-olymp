# 482 Укладка плиток
def f(param):
	if (param < 0):
		return 0
	elif (param == 0):
		return 1
	elif (param == 2):
		return 3
	return f(param - 2) * 4 - f(param - 4)


while True:
	n = int(input())
	if n == -1:
		break
	else:
		print(f(n))
