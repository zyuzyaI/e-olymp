# 8507 Сумма квадратов цифр
n=int(input())
m=0
for i in range(4):
    k=n%10
    n=n//10
    m+=k**2
print(m)
