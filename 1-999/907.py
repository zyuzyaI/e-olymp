# 907 Первый не больший чем 2,5
n1=int(input())
n=input().split()
c=[]
for i in n:
    i=float(i)
    c.append(i)
for i in range(n1):

    if c[i]<=2.5:

        print(i+1, '%.2f' %c[i])
        break
else:
    print('Not Found')
