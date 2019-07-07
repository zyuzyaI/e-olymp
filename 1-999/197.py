# 197 Відрізок і кола
import math
e = 10e-8
x1, y1, x2, y2 = map(int,input().split())
if math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)) == 0:
    d = 0
else:
    d = math.fabs((y2*x1-x2*y1)/math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)))
a = math.sqrt(x1*x1+y1*y1)
b = math.sqrt(x2*x2+y2*y2)
count = 0
if ((2*x1*x1-2*x1*x2+2*y1*y1-2*y1*y2<0) or (2*x2*x2-2*x1*x2+2*y2*y2-2*y1*y2<0)):
    count = int(max(a,b)+e)-int(min(a, b)-e)
else:
    count = int(a+e)-int(d-e)
    count = count+int(b+e)-int(d-e)
    if ((math.fabs(round(d)-d)<e) and (math.fabs(d)>e)):
        count -= 1
print(count)
