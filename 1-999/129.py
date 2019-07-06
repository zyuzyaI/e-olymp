# 129 Клітинки в колі
r = int(input())
k = 0
x = 0
y = 0
while x < r:
    x += 1
    y = 1

    while x**2 <= r**2 - y**2:
        k += 1
        y += 1

print(4*k)
