# 2663  Сортировка пузырьком
q=input()
mass=[int(i) for i in input().split()]
n=len(mass)
c=0
for i in range(1,n):
    for k in range(0,n-i):
        if mass[k]>mass[k+1]:
            mass[k],mass[k+1]=mass[k+1],mass[k]
            c+=1
print(c)
