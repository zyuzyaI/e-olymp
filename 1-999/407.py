# 407 Обмен
q = int(input())
for i in range(q):
	n=int(input())
	if n%3 == 0:
		print('GCV')
	elif n%3 == 1:
		print('VGC')
	elif n%3 ==2:
		print('CVG')
