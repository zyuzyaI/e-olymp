# 134Два кола - 2
x1,y1,r1,x2,y2,r2 = map(int,input().split())
count = 0
for x in range(-300,301):
    for y in range(-300,301):
        if ((x1-x)**2+(y1-y)**2 <= r1*r1) or ((x2-x)**2 + (y2-y)**2 <= r2*r2):
            count+=1
print(count)
