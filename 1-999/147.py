# 147 Кількість днів
from datetime import date
from math import fabs

d1,m1,y1 = map(int, input().split())
d2,m2,y2 = map(int, input().split())

a = date(y1,m1,d1)
b = date(y2,m2,d2)

print(int(fabs((b-a).days)+1))
