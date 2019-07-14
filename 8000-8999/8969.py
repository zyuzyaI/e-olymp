# 8969 169
n = int(input())


mass = [int(i) for i in input().split()]
print(mass[0], end=' ')
for i in range(1,n):
	print(mass[i] - mass[i-1], end=' ')
