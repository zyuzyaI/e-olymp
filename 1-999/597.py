# 597 Забавная игра
n = int(input())
c = str(bin(n)[2:])
k = c

d =0
for i in k:
    c = c[1:]+i
    if d < int(c,2):
        d = int(c,2)

print(d)
