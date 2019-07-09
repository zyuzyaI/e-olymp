# 947 Обратный порядок
n=int(input())
for i in range(3):
    k=n%10
    n=n//10
    print(k, end='')
