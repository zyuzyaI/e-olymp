# 8631 Количество максимальных цифр
n=input()
k2=len(n)
c=[]
n=int(n)
for i in range(k2):
    k1=n%10
    n=n//10
    c.append(k1)
a=c.count(max(c))

print(a)
