# 143 Точка і трикутник
n = input().split()
ox = float(n[0])
oy = float(n[1])
ax = float(n[2])
ay = float(n[3])
bx = float(n[4])
by = float(n[5])
cx = float(n[6])
cy = float(n[7])
a = (ax-ox) * (by-ay) - (ay-oy) * (bx-ax)
b = (bx-ox) * (cy-by) - (by-oy) * (cx-bx)
c = (cx-ox) * (ay-cy) - (cy-oy) * (ax-cx)


if a <= 0 and b <= 0 and c <= 0:
    print('1')
elif a >= 0 and b >= 0 and c >= 0:
    print('1')
else:
    print('0')
