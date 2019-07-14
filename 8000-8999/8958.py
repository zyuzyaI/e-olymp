# 8958 158
n = int(input())
mass = [int(i) for i in input().split()]
tmp = []
if n//2 == 0:
	print('NO')
else:
	print(n//2)
	for i in range(1,n,2):
		print(mass[i], end=' ')
