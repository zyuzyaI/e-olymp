# 935 Разложение трехзначного числа
n=int(input())
if n<0:
    n=-n
q=[]
for i in range(3):
    c=n%10
    n=n//10
    q.append(c)
q=q[::-1]
for i in q:
    print(i)
