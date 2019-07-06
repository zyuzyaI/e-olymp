# 142 Точка і відрізок
import math
n = input().split()
ox = float(n[0])
oy = float(n[1])
ax = float(n[2])
ay = float(n[3])
bx = float(n[4])
by = float(n[5])
oa = math.sqrt((ox-ax)**2+(oy-ay)**2)
ob = math.sqrt((ox-bx)**2+(oy-by)**2)
ab = math.sqrt((ax-bx)**2+(ay-by)**2)

if oa+ob == ab:
  print('1')
else:
  print('0')
