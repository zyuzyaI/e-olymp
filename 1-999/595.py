# 595 Новый Лабиринт Амбера
n = int(input())
mass = [int(i) for i in input().split()]
mass = [0]+mass
mass[1] = 0
for i in range(2,n+1):
	if (i - 3) >= 0:
		mass[i] = mass[i] + max(mass[i-2], mass[i-3])
print(mass[-1])
