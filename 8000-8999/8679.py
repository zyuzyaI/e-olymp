# 8679 Разделить на 3
n1=int(input())
n=input().split()
c=[]
for i in n:
    i=int(i)
    if i%3==0:
        print(int(i/3), end=' ')
    else:
        print(i, end=' ')
