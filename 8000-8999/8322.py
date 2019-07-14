# 8322 Сума - 1
n=int(input())
if n==1:
    c=[i for i in range(1,11)]

elif n==2:
    c=[i for i in range(2,21,2)]
elif n==3:
    c=[i for i in range(1,20,2)]
elif n==4:
    c=[i for i in range(4,41,4)]
elif n==5:
    c=[i for i in range(1,29,3)]
elif n==6:
    c=[i for i in range(5,51,5)]
print(sum(c))
