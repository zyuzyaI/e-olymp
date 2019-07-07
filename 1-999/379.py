# 379 Защита от сбоев
n=input()
cem=0
for i in n:
    if i == '1':
        cem+=1
if (cem%2 == 0 and n[-1] == 'e'):
    print(n[:-1]+'0')
else:
    if (cem%2 == 1 and n[-1] == 'o'):
        print(n[:-1]+'0')
    else:
        print(n[:-1]+'1')
