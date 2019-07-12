# 4746 Кафе "Хоботания"
n = int(input())

def sorter():
	tmp = True
	while tmp:
		tmp = False
		for i in range(n-1):
			if mass[i] < mass[i+1]:
				mass[i], mass[i+1] = mass[i+1], mass[i]
				tmp = True
	return mass

if n != 0:
	mass = [int(i) for i in input().split()]
	sorter()
	tmp = 0
	for i in range(n):
		if mass[i] - i > 0:
			tmp += mass[i] - i
		else:
			break
	print(tmp)
else:
	print(0)
