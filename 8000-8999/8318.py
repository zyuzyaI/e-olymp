# 8318 Удалите цифры
n=input()
c=[i for i in n if i!='3' and i!='9']
for j in c:
    print(j,end='')
