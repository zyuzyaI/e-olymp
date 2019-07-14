# 8519 Сумма четных цифр
n=input()
k=len(n)
n=int(n)
c=0
v=[]
for i in range(k):
    c=int(n%10)
    n=n//(10)
    v.append(c)
c=0
for i in v:
    if i%2==0:
        c+=i
print(c)
