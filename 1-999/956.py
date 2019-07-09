# 956 Площадь поверхности пирамиды 3
from math import sqrt
n=input().split()
v,h=float(n[0]),float(n[1])
sahe=sqrt(9*v*v+12*v*h*h*h)/h
print('%.1f' %sahe)
