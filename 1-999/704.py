# 704 Факториалы
from math import factorial as f

def fac(x):
	for i in (str(f(x)))[::-1]:
		if i != '0':
			return i

n = int(input())
for i in range(n):
	k = int(input())
	print(fac(k))
