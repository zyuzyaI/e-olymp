# 8506 Сумма нескольких действительных
n=input().split()
a,b,c,d=float(n[0]), float(n[1]),float(n[2]),float(n[3])
sps=('%.4f' %(a+b), '%.4f' %(a+b+c), '%.4f'%(a+b+c+d))
for j in sps:
    print(j)
