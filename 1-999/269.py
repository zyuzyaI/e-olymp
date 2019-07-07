# 269 Четыре окружности
a,b,c = map(int, input().split())
d=1/a+1/b+1/c+2*(a+b+c)**0.5/((a*b*c)**0.5)
d=1/d
print('%.4f' %d)
