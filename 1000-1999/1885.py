# 1885 Количество линий
n = (input())
k = 0
for i in n:
	if i == '-':
		k += 1
	elif i == '1':
		k += 2
	elif i == '0' or i == '6' or i == '9':
		k += 6
	elif i == '2' or i == '3' or i == '5':
		k += 5
	elif i == '4':
		k += 4
	elif i == '7':
		k += 3
	elif i == '8':
		k += 7
print(k)
