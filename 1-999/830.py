# 830 Простые числа
def primes(n):
	if n == 1 or n == 0:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	for i in range(3,(int(n**0.5) +1), 2):
		if n % i == 0:
			return False
	return True

x = input().split()
n, m = int(x[0]),int(x[1])

k = True
for i in range(min(n,m), max(n,m)+1):
	if primes(i):
		k = False
		print(i)
if k:
	print('Absent')
