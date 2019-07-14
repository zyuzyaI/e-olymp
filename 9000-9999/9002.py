# 9002 Любитель шоколода
from math import ceil as s
n, a, b = map(int, input().split())

print(s(n/2)*max(a,b) + (n - s(n/2))*min(a,b))
