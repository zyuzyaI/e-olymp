# 381 Страшное число
b,n = map(int, input().split())
a = int(b** (1.0/n))
if (a**n) == b:
	print(a)
else:
	Sol = b - int(a**n)
	Sag = int((a + 1)**n - b)
	print(a if Sol < Sag else  a+1)
