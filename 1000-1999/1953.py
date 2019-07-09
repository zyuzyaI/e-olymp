# 1953 Результаты олимпиады
def takeSecond(elem):
    return elem[1]
n=int(input())
k=input().split()
c=[]
for i in range(n):
    a=(int(i+1),int(k[i]))
    c.append(a)
c.sort(key=takeSecond, reverse=True)
for i in range(n):
    print(c[i][0], end=' ')
