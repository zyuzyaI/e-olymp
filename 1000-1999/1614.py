# 1614 Углы треугольника
import math
def Mesafe(x1,y1,x2,y2):
    return math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

def Sahe(a,b,c):
    return math.sqrt((a+b+c)*(a+b-c)*(a+c-b)*(b+c-a))/4.0

n=input().split()
x1,y1=int(n[0]),int(n[1])
n=input().split()
x2,y2=int(n[0]),int(n[1])
n=input().split()
x3,y3=int(n[0]),int(n[1])
a=Mesafe(x1, y1, x2, y2)
b=Mesafe(x1, y1, x3, y3)
c=Mesafe(x2, y2, x3, y3)

if a == max(a, b, c):
    bucaq =math.acos((b*b + c*c - a*a)/(2*b*c))
elif b == max(a, b, c):
    bucaq= math.acos((a*a + c*c - b*b)/(2*a*c))
else:
    bucaq=math.acos((a*a + b*b - c*c)/(2*a*b))
bucaq = bucaq*180/math.pi
print('%.6f' %bucaq)
