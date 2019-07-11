# 4741 Сортировка пузырьком - 2
def bubble_sort(mass):
	tmp = True
	counter = 0
	while  tmp:
		tmp = False
		for i in range(len(mass) - 1):
			if mass[i] > mass[i+1]:
				mass[i], mass[i+1] = mass[i+1], mass[i]
				tmp = True
				counter += 1
	return counter

n = int(input())
mass = [int(i) for i in input().split()]

print(bubble_sort(mass))
