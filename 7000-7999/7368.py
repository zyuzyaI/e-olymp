# 7368 Средний балл для фигуристов
n1=[int(i) for i in (input().split())]
c=[]
for i in range(n1[1]):
    n=[int(i) for i in (input().split())]
    ma=max(n)
    mi=min(n)
    c1=[]
    for j in n:
        if j!=mi:
            if j!=ma:
                c1.append(j)
    c.append(c1)
for j in c:
    print('%.2f' %(sum(j)/len(j)), end=' ')
