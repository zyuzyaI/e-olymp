# 036 Змей Горыныч
n=input().split()
a=int(n[0])
b=int(n[1])
k=0
if a==0:
  if b==0:
    k=0
  else:
    if b%2==0:
      k=int(b/2+b/4)
    if b%2==1:
      a1=a
      b1=b
      while ((b1/2)%2)!=0:
        b1+=1
        k+=1
        c=(b1/2)%2
      k=int(k+b1/2)
      a1=a1+b1/2
      k=int(k+a1/2)
else:
  if a%2==0:
    if b%2==0:
      a1=a
      b1=b
      while ((b1/2)%2)!=0:
        b1+=1
        k+=1
        c=(b1/2)%2
      k=int(k+b1/2)
      a1=a1+b1/2
      k=int(k+a1/2)

    if b%2==1:
        a1=a
        b1=b
        while ((b1/2)%2)!=0:
            b1+=1
            k+=1
            c=(b1/2)%2
        k=int(k+b1/2)
        a1=a1+b1/2
        k=int(k+a1/2)

  if a%2==1:
    if b==0:
      k=-1
    else:
      a1=a
      b1=b
      while ((b1/2)%2)!=1:
        b1+=1
        k+=1
      k=int(k+b1/2)
      a1=a1+b1/2
      k=int(k+a1/2)
if b<0:
    k=-1
print(k)
