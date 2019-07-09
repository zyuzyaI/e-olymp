# 1604 Произведение чётных цифр числа
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
m=1
q1=[]
for i in q:
    if i%2==0:
       m*=i
       q1.append(i)

if len(q1)==0:
    print('-1')
else:
    print(m)
