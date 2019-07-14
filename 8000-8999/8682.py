# 8682 Удалить четные цифры
n=input()
c=len(n)
n=int(n)
k=[]
for i in range(c):
    a=n%10
    n=n//10
    if a%2!=0:
        k.append(a)
k=k[::-1]
if k==[]:
    k.append(0)
for i in k:
    print(i, end='')
