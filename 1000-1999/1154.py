# Кружок хорового пения 1154
def f(a, b):
	while a*b != 0:
		if a > b:
			a %= b
		else:
			b %= a
	return a + b

file = open('input.txt')
outputfile = open('output.txt', 'w')
for i in file:
	s = i.split()
	a, b = int(s[0]), int(s[1])
	outputfile.write(('YES' if f(a, b) == 1 else 'NO') +'\n')
outputfile.close()