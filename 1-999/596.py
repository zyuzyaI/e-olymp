# 596 Торговые сделки в Амбере
def dec_to_base(N, base):
    if not hasattr(dec_to_base, 'table'):
        dec_to_base.table = '0123456789ABCDEF'
    x, y = divmod(N, base)
    return dec_to_base(x, base) + dec_to_base.table[y] if x else dec_to_base.table[y]

def suma_n(n):
	tmp = '0123456789'
	n = str(n)
	k = int(0)
	for i in n:
		if i in tmp:
			k += int(i)
		elif i == 'A':
			k += 10
		elif i == 'B':
			k += 11
		elif i == 'C':
			k += 12
		elif i == 'D':
			k += 13
		elif i == 'E':
			k += 14
		elif i == 'F':
			k += 15
	return(k)


n1, p1 = map(int, input().split())
n2, p2 = map(int, input().split())

N1 = dec_to_base(n1, p1)
N2 = dec_to_base(n2, p2)

if suma_n(N1) == suma_n(N2):
	print(suma_n(N1))
else:
	print(0)
