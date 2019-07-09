# 1605 Вторая цифра числа
n=input()
c=len(n)
n=int(n)
if n<0:
    n=-n
    c=c-1
q=[]
for i in range(c):
    k=n%10
    n=n//10
    q.append(k)
if len(q)>=2:
    print(q[-2])
else:
    print(0)
