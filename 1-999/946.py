# 946 Площадь четырёхугольника
import math
n=input().split()
x1,y1,x2,y2,x3,y3,x4,y4=int(n[0]),int(n[1]),int(n[2]),int(n[3]),int(n[4]),int(n[5]),int(n[6]),int(n[7])
s=round(0.5*(math.fabs((x1-x2)*(y1+y2)+(x2-x3)*(y2+y3)+(x3-x4)*(y3+y4)+(x4-x1)*(y4+y1))))

print((s))
