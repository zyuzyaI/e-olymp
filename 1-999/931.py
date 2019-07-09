# 931 Отношение произведения к сумме
n=input()
b=0
m=1
for i in n:
    i=int(i)
    b+=i
    m*=i
n=int(n)
k=float(m/b)
print('%.3f' %k)
