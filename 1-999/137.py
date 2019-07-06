# 137 НСД
k = int(input())
v = input().split()
n = [int(i) for i in v]


a = n[0]
for i in range(len(n)):
    b = n[i]
    while b:
        a,b = b,a%b
print(a)
