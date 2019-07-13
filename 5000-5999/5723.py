# 5723 Ветренная погода 3
q=int(input())
n=input().split()
k=len(set(n))
if k==1:
    print(0)
else:
    print(k)
