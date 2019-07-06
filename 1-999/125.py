# 125 Олімпіада
n = input().split()
n1 = input().split()
t11 = int(n[0])
t12 = int(n[1])
t13 = int(n[2])
t21 = int(n1[0])
t22 = int(n1[1])
t23 = int(n1[2])
T1 = t11*3600 + t12*60 + t13
T2 = t21*3600 + t22*60 + t23
T = T2 - T1
k1 = T // 3600
k2 = (T-3600*k1) // 60
k3 = T-3600*k1 - 60*k2
print(k1, k2, k3)
