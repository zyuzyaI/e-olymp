# 062 Факториал
n=int(input())
s=1
k=1
while True:
    s=k*s
    k+=1
    if n==s:
        break
print(k-1)
