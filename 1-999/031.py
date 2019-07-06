# 031 Суеверный Дед Мороз
q=int(input())
c2=[16, 18, 19, 25, 1, 2, 3, 4, 7, 8, 13, 14]
c3=[21, 24, 27, 10]
count=0
for i in range(q):
    year1,year2=map(int,input().split())
    for j in range(year1,year2+1):
        if j%28 in c2:
            count+=2
        elif j%28 in c3:
            count+=3
        else:
            count+=1
print(count)