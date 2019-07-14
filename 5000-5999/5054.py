# 5054 Високосный ли год?
n = int(input())
if n % 4 == 0:
	if n % 400 == 0:
		print('YES')
	elif n % 100 == 0:
		print('NO')
	else:
		print('YES')
else:
	print('NO')
