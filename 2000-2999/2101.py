# 2101 Междугородние билеты
from math import fabs as f
q=input()
c=4
if len(q)==4:
    pass
else:
    if len(q)==1:
        q='000'+q
    elif len(q)==2:
        q='00'+q
    elif len(q)==3:
        q='0'+q
for i in range(1,len(q)):
        c+=f(int(q[i-1])-int(q[i]))
print(int(c))
