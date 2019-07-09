# 1965 Шеренга
n = int(input())
mass = [int(i) for i in input().split()]
petya = int(input())
mass.sort(reverse=True)
for i in range(n):
	if petya > mass[i]:
		print(i+1)
		break
else:
	print(n+1)
