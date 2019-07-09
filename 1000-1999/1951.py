# 1951 IP-адрес
n=input()
for i in range(len(n)-1):
    if n[i]==n[i+1]=='.':
        print(0)
        break
else:
    if n[0]=='.':
	    print(0)
    elif n[-1]=='.':
	    print(0)
    else:
	    k=0
	    n=n.split('.')
	    for i in n:
		    if 0<=int(i)<=255:
			    k+=1
		    else:
			    print(0)
			    break
	    if k==4:
		    print(1)
