# 2804 Квадратные числа
n=input()
k=0
for i in n:
    k+=int(i)
if (k**0.5)%1==0:
    print('Yes')
else:
    print('No')
