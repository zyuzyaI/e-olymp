# 135 НСК
def ngs(a,b):
	m = a * b
	while a * b != 0:
		if a > b:
			a = a % b
		else:
			b = b % a
	return m // (a + b)

n = int(input())
mass = [int(i) for i in input().split()]

k = mass[0]
for i in range(1,n):
	k = ngs(k,mass[i])
print(k)
