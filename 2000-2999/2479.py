# 2479 Баланс скобок
n = int(input())
for i in range(n):
	test = input()
	mass = []

	tmp = False
	for j in range(len(test)):
		if test[j] == '(' or test[j] == '[':
			mass.append(test[j])
		else:
			if test[j] == ')':
				try:
					if mass.pop() != '(':
						tmp = True
						break
				except IndexError:
					tmp = True
					break
			if test[j] == ']':
				try:
					if mass.pop() != '[':
						tmp = True
						break
				except IndexError:
					tmp = True
					break
