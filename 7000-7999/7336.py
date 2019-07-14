# 7336 Пиріжки
x=input().split()
a=int(x[0])
b=int(x[1])
n=int(x[2])
a=a*100
k=a+b
q=k*n

k1=q//100
k2=q%100
print(k1, k2)
