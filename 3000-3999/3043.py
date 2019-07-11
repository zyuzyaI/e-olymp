# 3043 Class Statistics
n = int(input())
for i in range(1, n+1):
	k = 0
	mass = [int(i) for i in input().split()]
	mass = mass[1:]
	mass.sort()
	for j in range(1,len(mass)):
		if k < abs(mass[j-1] - mass[j]):
			k = abs(mass[j-1] - mass[j])
	print('Class {}'.format(i))
	print('Max {}, Min {}, Largest gap {}'.format(max(mass), min(mass), k))
