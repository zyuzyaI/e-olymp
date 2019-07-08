# 462 Клавиатура
q = int(input())

our = [int(i) for i in input().split()]

n = int(input())
our_keys = [int(i) for i in input().split()]
for i in our_keys:
	our[i-1] -= 1
for i in our:
	if i < 0:
		print('yes')
	else:
		print('no')
