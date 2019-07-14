# 8571 Подсчитать буквы
n=input()
n=n.lower()
q=str(input())

c=0
for i in n:
    if i==q[0] :
        c+=1
print(c)
