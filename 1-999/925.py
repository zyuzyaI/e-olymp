# 925 Периметр и площадь треугольника
import math
n=input().split()
c=[]
for i in n:
    c.append(float(i))
x1,y1,x2,y2,x3,y3=c

a=math.sqrt((x2-x1)**2+(y2-y1)**2)
b=math.sqrt((x3-x2)**2+(y3-y2)**2)
d=math.sqrt((x1-x3)**2+(y1-y3)**2)

p=(a+b+d)


s=((p/2*(p/2-a)*(p/2-b)*(p/2-d))**0.5)







print('%.4f %.4f' %(p, s))
