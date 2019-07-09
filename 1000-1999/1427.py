# 1427 Калькулятор
n=input()
v=[]
c=[]
k=''
for i in n:
    if i!='-'and i!='+':
        k+=i
    elif i=='-':
        v.append(k)
        c.append(i)
        k=''
    elif i=='+':
        v.append(k)
        c.append(i)
        k=''
v.append(k)
res=int(v[0])
for i in range(len(c)):
    if c[i]=='-':
        res-=int(v[i+1])
    else:
        res+=int(v[i+1])
print(res)
