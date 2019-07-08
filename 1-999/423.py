# 423 Премия
def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]

q = int(input())
for i in range(q):
	mass = input().split()
	age = mass[0]
	if len(age) == 2:
		base =  int(age[1])+2
	else:
		base = int(age[0])+2
	print(convert_base(mass[1], 10, base))
