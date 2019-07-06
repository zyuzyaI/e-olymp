# Сортировка времени №972 
def mass_sort(mass):
	for i in range(len(mass)):
		
		for j in range(i+1, len(mass)):
			if mass[i][0] > mass[j][0]:
				mass[i], mass[j] = mass[j], mass[i]
			elif mass[i][0] == mass[j][0]:
				if mass[i][1] > mass[j][1]:
					mass[i], mass[j] = mass[j], mass[i]
				elif mass[i][1] == mass[j][1]:
					if mass[i][2] > mass[j][2]:
						mass[i], mass[j] = mass[j], mass[i]
	return mass

n = int(input())
mass = []
for i in range(n):
	mass.append([int(i) for i in input().split()])

mass = mass_sort(mass)
for i in range(n):
	print(*mass[i])


