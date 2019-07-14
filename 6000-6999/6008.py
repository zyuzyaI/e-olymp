# 6008 Обратные треугольные числа
k = 0
while True:
	k += 1
	n = int(input())
	if n == -1:
		break
	else:
		x = (-1 + (1 + 8 * n) ** 0.5) / 2
		if x == int(x):
			print('Case ' + str(k) + ': '  + str(int(x)))
		else:
			print('Case ' + str(k) + ': bad')
