# 8858 058
n = int(input())
if n < 0:
	n = - n
n = str(n)[:]
if n[-1] != '0':
	print(n[-1] + n[1] + n[0])
else:
	print(n[1] + n[0])
