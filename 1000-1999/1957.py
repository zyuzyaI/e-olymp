# 1957 Серебряная медаль
n=int(input())
c=input().split()
b=[int(i) for i in c]


v=list(set(b))
v.sort(reverse=True)
print(v[1])
