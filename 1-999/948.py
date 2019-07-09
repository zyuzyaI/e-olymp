# 948 Площадь и объем пирамиды
n=input().split()
d,p=float(n[0]),float(n[1])
s=d*d+2*d*(p*p-d*d/4)**0.5
v=(1/3)*d*d*((p*p-(2*d*d)/4)**0.5)
print('%.3f %.3f' %(s,v))
