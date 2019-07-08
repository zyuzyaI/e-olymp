# 496 Перестановка
q = int(input())
for i in range(q):
	mass = input().split()
	mass1 = [x.lower() for x in mass[0]]
	mass2 = [x.lower() for x in mass[1]]

	mass1.sort()

	mass2.sort()
	if mass1 == mass2:
		print('Yes')
	else:
		print('No')
