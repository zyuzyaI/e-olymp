# 8824 024
a, b = map(int, input().split())
if a < b:
	for i in range(a+1, b):
		print(i , end=' ')
elif a > b:
	for i in range(a-1, b, -1):
		print(i , end=' ')
