# 2108 Разворот последовательности
x = input().split()
a = []
for i in range(len(x)):
    a.append(int(x[i]))
a=a[::-1]
for i in a:
    print(int(i), end=' ')
