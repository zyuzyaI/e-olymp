# 130 Прямокутник
import math
n = input().split()
x1,x2,x3 = int(n[0]),int(n[2]),int(n[4])
y1,y2,y3 = int(n[1]),int(n[3]),int(n[5])


if x1 == x2:
    x4 = x3
if x1 == x3:
    x4 = x2
if x2 == x3:
    x4 = x1

if y1 == y2:
    y4 = y3
if y1 == y3:
    y4 = y2
if y2 == y3:
    y4 = y1

else:
    AB = math.sqrt(((x1-x2)**2) + ((y1-y2)**2))
    AC = math.sqrt(((x1-x3)**2) + ((y1-y3)**2))
    BC = math.sqrt(((x2-x3)**2) + ((y2-y3)**2))
    if AB > AC and AB > BC:
        x4 = x1-x3+x2
        y4 = y1-y3+y2
    if AB < AC and AC > BC:
        x4 = x1-x2+x3
        y4 = y1-y2+y3
    if AB < BC and AC < BC:
        x4 = x3-x1+x2
        y4 = y3-y1+y2

print(x4, y4)
