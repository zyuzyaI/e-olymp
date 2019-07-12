# 4745 Скейтборд
n = int(input())
mass = [int(i) for i in input().split()]
counter = 0
for i in range(1, n-1):
	if mass[i] > mass[i-1] and mass[i] > mass[i+1]:
		counter += 1
print(counter)
