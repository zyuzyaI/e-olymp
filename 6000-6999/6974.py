#6974 Добро против Зла


n = int(input())
i = 1
good_power = [1, 2, 3, 3, 4, 10]
evil_power = [1, 2, 2, 2, 3, 5, 10]
for j in range(n):
	good = [int(k) for k in input().split()]
	evil = [int(k) for k in input().split()]
	g = 0
	e = 0
	for item in range(6):
		g += good[item]*good_power[item]

	for item in range(7):
		e += evil[item]*evil_power[item]

	if g > e:
		print('Battle {}: Good triumphs over Evil'.format(i))
	elif g < e:
		print('Battle {}: Evil eradicates all trace of Good'.format(i))
	elif g == e:
		print('Battle {}: No victor on this battle field'.format(i))

	i += 1
