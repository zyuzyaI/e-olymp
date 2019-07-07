# 358 Прогресс в артиллерии начинается
n=input()
k=len(n)
n=int(n)
ans=0
for i in range(k):
	c=n%10
	if c==0:
		ans+=6
	elif c==1:
		ans+=2
	elif c==2:
		ans+=5
	elif c==3:
		ans+=5
	elif c==4:
		ans+=4
	elif c==5:
		ans+=5
	elif c==6:
		ans+=6
	elif c==7:
		ans+=3
	elif c==8:
		ans+=7
	elif c==9:
		ans+=6
	n//=10

print(ans)
