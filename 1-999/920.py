# 920 Используй функцию
n=input().split()
x=float(n[0])
y=float(n[1])
z=float(n[2])
k=min(max(x,y), max(y,z), x+y+z)

print('%.2f' %k)
