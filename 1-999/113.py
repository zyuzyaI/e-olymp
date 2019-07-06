# 113 Кульки
k = int(input())
c = []
n = []
n1 = input().split()
for i in n1:
    n.append(int(i))

c1 = n.count(1)
c2 = n.count(2)
c3 = n.count(3)
c4 = n.count(4)
c5 = n.count(5)
c6 = n.count(6)
c7 = n.count(7)
c8 = n.count(8)
c9 = n.count(9)
if c1 != 0:
    c.append(c1)
if c2 != 0:
    c.append(c2)
if c3 != 0:
    c.append(c3)
if c4 != 0:
    c.append(c4)
if c5 != 0:
    c.append(c5)
if c6 != 0:
    c.append(c6)
if c7 != 0:
    c.append(c7)
if c8 != 0:
    c.append(c8)
if c9 != 0:
    c.append(c9)
c.sort()
print(k-(c[-1]))
