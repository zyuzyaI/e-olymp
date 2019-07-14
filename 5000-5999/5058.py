# 5058 Скобочная последовательность
mass = input()
work_mass = []
tmp = True
for i in mass:
	if i in ('([{'):
		work_mass.append(i)
	elif i in (')]}'):
		if len(work_mass) == 0:
			tmp = False
			break
		elif i == ')':
			if work_mass.pop() != '(':
				tmp = False
				break
		elif i == ']':
			if work_mass.pop() != '[':
				tmp = False
				break
		elif i == '}':
			if work_mass.pop() != '{':
				tmp = False
				break
if tmp and not work_mass:
	print('yes')
else:
	print('no')
