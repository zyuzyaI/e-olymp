# 957 Квадратный корень
n=int(input())
a=n//100
b=(n//10)%10
c=n%10
q=(a+b+c)**0.5
print('%.3f' %q)
