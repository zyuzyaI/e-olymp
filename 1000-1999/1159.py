# 1159 День рождения
n=int(input())
i=((13*n)%31)
j=-5*n
j=(j%12)
i=31 if i==0 else i
j=12 if j==0 else j
ki=len(str(i))
kj=len(str(j))
ci=('0%s/' %i) if ki==1 else ('%s/' %i)
cj=('0%s' %j) if kj==1 else ('%s' %j)
print(ci,cj, sep='')
