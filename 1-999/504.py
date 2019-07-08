# 504 Парковка
q=int(input())

for i in range(q):
    n=input()
    n='0'+n+'0'*2
    s=0
    for j in range(len(n)-2):
        if n[j]=='-' and n[j+1]!='S' and n[j-1]!='S' and n[j+1]!='B' and n[j+2]!='B':
            s+=1
    print(s)
