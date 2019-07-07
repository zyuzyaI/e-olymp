# 192 Просто Фібоначчі
n = int(input())
a = 1
b = 1
c = 2
count = 0
while count < n:
    x = True
    c = a+b
    a = b
    b = c
    for j in range(2, int((c**0.5))+1):
        if (c%j) == 0:
            x = False
    if x:
        count += 1

print(c)
