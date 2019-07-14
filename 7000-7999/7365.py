# 7365 Молоко и пирожок
n1=int(input())
n=input().split()
c=[float(i) for i in n]
k=0
for i in c:
    if i<30:
        k+=1
count=int((2 * k + 8) / 9)
print(count, k)
