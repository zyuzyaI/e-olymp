# 145 Квадрати
n1 = int(input())
n = input().split()
n.sort()
k = 0
k1 = 0
c = []
for i in range(n1):
    if n[i-1] !=n [i]:
        c.append(n[i])
for j in range(len(c)):
    k=n.count(c[j])
    if k >= 4:
        k1 += k//4
    k = 0

print(k1)
