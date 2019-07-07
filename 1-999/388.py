# 388 Превращение
n=int(input())
q=0
while n!=1:
    if n%2==0:
        n/=2
        q+=1
    else:
        n+=1
        q+=1
print(q)
