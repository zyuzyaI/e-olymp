# 138 Банкомат
n = int(input())
k = 0
c = 0
if n%10 == 0:
    while  n >= 500:
        n -= 500
        k += 1
    while n >= 200:
        n -= 200
        k += 1
    while  n >= 100:
        n -= 100
        k += 1
    while n >= 50:
        n -= 50
        k += 1
    while  n >= 20:
        n -= 20
        k += 1
    while n >= 10:
        n -= 10
        k += 1
else:
    k = -1
print(k)
