# 8522 Делимость
n=input().split()
a=int(n[0])
b=int(n[1])
if a%b!=0:
    print(a//b, a%b)
else:
    print('Divisible')
