# 108 Середнє з чисел
n = input().split()
a = int(n[0])
b = int(n[1])
q = int(n[2])
c = []
c.append(a)
c.append(b)
c.append(q)
c.remove(max(c))
c.remove(min(c))
k = int(c[0])
print(k)
