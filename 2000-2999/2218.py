# 2218 Монетки
n=int(input())
a=0
b=0
for i in range(n):
    m=int(input())
    if m==1:
        a+=1
    else:
        b+=1
print(min(a,b))
