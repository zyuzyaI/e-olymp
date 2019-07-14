# 8970 170
n = int(input())


mass = [int(i) for i in input().split()]
new_mass_right = mass[:n//2]
if n % 2 == 1:
	new_mass_left = mass[n//2 + 1:]
else:
	new_mass_left = mass[n//2:]
#mass = mass[::-1]

for i in range(n//2):
	print(str(new_mass_right[i])+ ' ' + str(new_mass_left[i]), end=' ')
if n % 2 == 1:
	print(mass[n//2])
