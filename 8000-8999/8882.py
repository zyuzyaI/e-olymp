# 8882 082
mass = [int(i) for i in input().split()]
if mass[0] == mass[1] and mass[0] == mass[2] and mass[0]  == mass[3]:
	print(mass[0] ** 2)
else:
	print('No')
