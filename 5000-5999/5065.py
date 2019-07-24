# 5065 Взрывоопасность 2
n = int(input())
mass = [2,3] + [0]*(n)
for i in range(2, n+1):
	mass[i] = mass[i-1] +  mass[i-2]
print(mass[n-1])
