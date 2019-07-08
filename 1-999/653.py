# 653 Треугольник
def Right(a,b,c, tmp=''):
	if a == max(a, b, c):
		return a*a == b*b + c*c
	if (b == max(a, b, c)):
		return b*b == a*a + c*c
	if (c == max(a, b, c)):
		return c*c == a*a + b*b
	return False

def Yoxla(a, b, c, tmp=''):
	if (a == max(a, b, c)):
		return a < b + c
	if b == max(a, b, c):
		return b < a + c
	if (c == max(a, b, c)):
		return c < a + b
	return False

def ItiKor(a, b, c,tmp=''):
	if (a == max(a, b, c)):
		if (a*a < b*b + c*c):
			tmp=("ACUTE")
			return tmp
		tmp=("OBTUSE")
		return tmp
	if (b == max(a, b, c)):
		if (b*b < a*a + c*c):
			tmp=("ACUTE")
			return tmp
		tmp=("OBTUSE")
		return tmp
	if (c == max(a, b, c)):
		if (c*c < a*a + b*b):
			tmp=("ACUTE")
			return tmp
		tmp=("OBTUSE")
		return tmp
	tmp=("")
	return tmp

a, b, c = map(int, input().split())

if Yoxla(a, b, c, tmp=''):
	if Right(a, b, c):
		print('RIGHT')
	else:

		if ItiKor(a, b, c) != '':
			print(ItiKor(a, b, c))
		else:
			print('IMPOSSIBLE')
else:
	print('IMPOSSIBLE')
