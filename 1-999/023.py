# 23 Новогодняя елка
def Addim(x,y):
    t=1
    j=1
    while (j <= y):
        t=t*x
        j+=1
    return t
def Say(n,k):
    if (n==2):
        return k*(k - 1)
    return k*Addim(k-1,n-1)-Say(n - 1, k)
def Yoxla(n,k):
    if (n==1):
        return k
    elif ((k==1) or ((n%2==1) and (k==2))):
        return -1
    elif ((k==2) and (n%2==0)):
        return 2
    return Say(n,k)
n,k=map(int,input().split())
say=0
print(Yoxla(n, k))