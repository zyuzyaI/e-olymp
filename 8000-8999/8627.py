# 8627 Сумма соседей
n=input().split()
c=[]
c.append(n[0])
c.append((int(n[0])+int(n[2])))
c.append(int(n[1])+int(n[3]))
c.append(int(n[2])+int(n[4]))
c.append(n[4])
for i in c:
    print(i, end=' ')
