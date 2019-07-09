# 958 Площадь поверхности пирамиды 4
from math import sqrt
from math import cos
from math import sin
from math import pi

n=input().split()
b,a=float(n[0]),int(n[1])
a=a*pi/180
sahe=2*b*b*cos(a)*(cos(a)+sqrt(1+sin(a)*sin(a)))
print('%.3f' %sahe)
