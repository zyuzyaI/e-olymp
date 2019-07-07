# 179 Розподілення
from math import fabs as f
q = int(input())
n = [int(i) for i in input().split()]
m = [int(i) for i in input().split()]
tmp = 0
for i in range(q):
    tmp += f(n[i]-m[i])
print(int(tmp/2))
