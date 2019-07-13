# 5713 Ветреная погода
n=int(input())
k=input().split()
c=[int(i) for i in k]
print(max(c)-min(c))
