# 7670 Степан і похід в магази
n=input().split()
d1=int(n[0])
d2=int(n[1])
d3=int(n[2])
if d1<d2:
    s=d1
else:
    s=d2
if d1+d2>d3:
    s=s+d3
else:
    s=s+d1+d2
if d1>d2:
    s=s+d1
else:
    s=s+d2
if (d3+d1)<d2:
    s=2*(d1+d3)
if (d3+d2)<d1:
    s=2*(d3+d2)
print(s)
