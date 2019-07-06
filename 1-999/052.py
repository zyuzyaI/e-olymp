# 052 Сыр для Анфисы
from math import pi, tan, sqrt,cos,sin
q=input().split()
a,b,z=int(q[0]),int(q[1]),int(q[2])
if (z!=0) and (z!=90):
    if (1/(tan (z*pi/180))>a/sqrt(2)/b):
        s=(a*a/2)/cos(z*pi/180)
    else:
        s=(a*sqrt(2)-b*1/(tan(z*pi/180)))*b/sin(z*pi/180)
elif (z == 0):
    s=0
elif (z == 90):
    s=a*b*sqrt(2)

print('%.3f' %s)
