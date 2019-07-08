# 670 Поиск палиндромов
n = int(input())
mass = input()
counter = 0

for i in range(len(mass)-(n-1)):
    tmp = mass[i:i+n]
    if tmp == tmp[::-1]:
        counter += 1
print(counter)
