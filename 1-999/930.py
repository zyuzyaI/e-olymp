# 930 Номер мобильного телефона
n=input()
a=[]
if '0'  not in n:
    a.append('0')
if '1'  not in n:
    a.append(1)
if '2'  not in n:
    a.append(2)
if '3'  not in n:
    a.append(3)
if '4'  not in n:
    a.append(4)
if '5'  not in n:
    a.append(5)
if '6'  not in n:
    a.append(6)
if '7'  not in n:
    a.append(7)
if '8'  not in n:
    a.append(8)
if '9'  not in n:
    a.append(9)
print(len(a))
for i in a:
    print(i, end=' ')
