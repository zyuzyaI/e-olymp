# 1955 Календарь
import calendar
n1=input().split()
n2=input().split()
d1,m1,y1=int(n1[0]),int(n1[1]),int(n1[2])
d2,m2,y2=int(n2[0]),int(n2[1]),int(n2[2])
k=calendar.leapdays(y1, y2)
from datetime import date
a = date(y1,m1,d1)
b = date(y2,m2,d2)
c=(b-a).days
print((int(c)-k)//(365))
