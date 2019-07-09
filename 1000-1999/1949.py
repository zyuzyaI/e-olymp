# 1949 Торт
n = int(input())
if n%2 == 0 or n == 1:
	if n == 1:
		print(0)
	else:
		print(n//2)
else:
	print(n)
