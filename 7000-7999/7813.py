# 7813 Кот, собака и заяц
n1=input().split()
a,b,c=int(n1[0]),int(n1[1]),int(n1[2])
k=(a-b+c)/2
d=(b+a-c)/2
r=(c-a+b)/2
print('%.2f %.2f %.2f' %(k,d,r))
