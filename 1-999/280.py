# 280 Уборка территории
n=[int(i) for i in input().split()]
a = max(n)
b = min(n)
while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a
print(a+b)
