# 571 Наибольший общий делитель
def gcb(a, b):
	while a*b != 0:
		if a > b:
			a = a%b
		else:
			b = b%a
	return a+b

q = int(input())
if q > 1:

	mass = [int(i) for i in input().split()]
	x = gcb(mass[0],mass[1])
	for i in range(1, q):
		x = gcb(x,mass[i])
	print(x)
else:
	if q == 0:
		print(0)
	elif q ==1:
		mass = int(input())
		print(mass)
