# 594 Текстовая статистика
def f(mass):
    excep = ['0','1','2','3','4','5','6','7','8','9','.',',',
    '!','?','#','-']
    our_mass = []
    for i in mass:
        b = []
        for j in i:
            if j in excep:
                if len(b) != 0:
                    our_mass.append(b)
                    b=[]
            else:
                b.append(j)
        if len(b) != 0:
            our_mass.append(b)
    return our_mass


mass = [str(i) for i in input().split()]
mass = f(mass)
if len(mass) == 0:
	print('%.9f' %(0))
else:
	k = 0
	for i in mass:
		k += len(i)
	print('%.9f' %(k/len(mass)))
