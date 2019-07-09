# 1118 Арбузы
q=int(input())
if q<=1:
    print('Ooops!')
else:
    n=[int(i) for i in (input().split())]
    print(min(n),max(n))
