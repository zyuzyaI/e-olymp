# 8316 Сортировка букв
c=input()
n=[i for i in c]
n.sort()
n1=n[::-1]
for i in n:
    print(i,end='')
print()
for j in n1:
    print(j, end='')
