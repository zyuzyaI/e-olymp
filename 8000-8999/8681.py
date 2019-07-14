# 8681 Произведение ненулевых цифр
n=input()
c=len(n)
n=int(n)
k=1
for i in range(c):
    if n%10!=0:
        k*=n%10
    n=n//10
print(k)
