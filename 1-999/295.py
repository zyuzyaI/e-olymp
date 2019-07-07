# 295 Круг
r = int(input())
count = 0
for y in range(r+1):
    count += int((r**2 - y*y)**0.5)

count = 4 * count + 1
print(count)
