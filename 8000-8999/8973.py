# 8973 173
n = int(input())
mass = [int(i) for i in input().split()]
new_mass = []
for i in range(len(mass)):
	if mass[i:].count(mass[i]) == 1:
		new_mass.append(mass[i])
print(*new_mass)
