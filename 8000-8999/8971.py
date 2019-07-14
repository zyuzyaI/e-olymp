# 8971 171
n = int(input())
mass = [int(i) for i in input().split()]
new_mass = []
for i in range(n):
	if mass[i] not in new_mass:
		new_mass.append(mass[i])
if new_mass:
	print(*new_mass)
else:
	print('NO')
