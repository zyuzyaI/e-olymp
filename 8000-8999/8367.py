#8367 Таксі
from decimal import Decimal
def gcd(a, b):
	while b * a != 0:
		if a > b:
			a %= b
		else:
			b %= a
	return a+b

numer = Decimal(input())
n = str(numer)

denomer =  10**(len(n) - 2) if len(n) > 1 else 1
numer = numer * denomer

GCD =  gcd(numer, denomer)
numer /= GCD
denomer /= GCD
remainder =  numer % denomer
numer -= remainder
fraction = int(numer / denomer)
print(int(denomer))

if numer == 5:

	print(0, 0, 0, 0, 1)
else:
	for i in range(1,5):
		if i == fraction:
			print(int(denomer - remainder), end=' ')
	
			if (fraction != 5):
				print(int(remainder), end=' ' )
		else:
			
			print(0, end=' ')