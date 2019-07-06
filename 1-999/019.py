# 19 Степень симметрии
n=input()
k=len(n)
c=0
for i in range(1,k//2+1):
    if n[0-i]==n[i-1]:
        c+=1
if k%2!=0:
    c+=1
print(c)