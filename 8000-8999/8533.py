# 8533 Числа с разными цифрами
n=input().split()
a=int(n[0])
b=int(n[1])
c=0
q=[]
for i in range(a,b+1):
    k=i
    for j in range(4):
        c=i%10
        i=i//10
        q.append(c)
    if (q[0]==q[1] or q[0]==q[2] or q[0]==q[3]) or q[1]==q[2] or q[1]==q[3] or q[2]==q[3]:
        pass
    else:
        print(k, end=' ')
    q=[]
