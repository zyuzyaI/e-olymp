# 1753 Младший бит
n=1
while True:
    n=int(input())
    if n==0:
        break
    c=bin(n)

    f=[]
    for i in range(len(c)-1,-1,-1):

        if c[i]!='1':
            f.append((c[i]))
        else:
            break
    f.append(1)
    f.reverse()
    f=[str(i) for i in f]
    z=''.join(f)
    m=int(z,2)
    print(m)
