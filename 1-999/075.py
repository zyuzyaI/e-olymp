# 075 Пірати і монети
q=input().split()
a=int(q[0])
m=int(q[1])
k=0
while True:
    k+=1
    m-=a
    a+=1
    if m==2*a:
        break

print(k+1)
