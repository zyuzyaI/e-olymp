# 314 A + B ?
q=int(input())
for i in range(q):

    n=input()
    k=0
    for i in n:
        if i=='-':
           k=1
    if k==1:
        n=n.split('-')
        a=int(n[0])
        b=int(n[1])
        print(a-b)
    else:

        n=n.split('+')

        a=int(n[0])
        b=int(n[1])
        print(a+b)
