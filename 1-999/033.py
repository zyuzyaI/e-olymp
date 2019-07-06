# 033 Любимые числа Деда Мороза
def f(n):
    n=str(n)
    for i in range(len(n)-1):
        if n[i]=='1' and n[i+1]=='3':
            return False
    return True
a=[True]*500001
a[0]=a[1]=False
for k in range(2,500001):
    if a[k]:
        for m in range(2*k,500001,k):
            a[m]=False
n,b=map(int,input().split())
say=0
for i in range(min(n,b),max(n,b)+1):
    if a[i] and f(i):
        say+=1
print(say)