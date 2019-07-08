# 490 Кодирование
n = input()
print(n[0], end='')
for i in range(1,len(n)):
	if n[i-1] == n[i]:
		print('0', end='')
	else:
		print('1', end='')
