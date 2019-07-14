# 8680 Четные соседи
n1=int(input())
n=input().split()
k=0
for i in range(1,n1-1):
    if int(n[i-1])%2==0 and int(n[i+1])%2==0:
        k+=1
print(k)
