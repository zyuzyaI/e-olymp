# 144 Чотирикутник
import math
n = input().split()
k = 0
ax = float(n[0])
ay = float(n[1])
bx = float(n[2])
by = float(n[3])
cx = float(n[4])
cy = float(n[5])
dx = float(n[6])
dy = float(n[7])
a = (ax-dx) * (bx-ax) + (ay-dy) * (by-ay)
if a == 0:
    k += 1
b = (bx-ax) * (cx-bx) + (by-ay) * (cy-by)
if b == 0:
    k += 1
c = (cx-bx) * (dx-cx) + (cy-by) * (dy-cy)
if c == 0:
    k += 1
d = (dx-cx) * (ax-dx) + (dy-cy) * (ay-dy)
if d == 0:
    k += 1
print(k)
