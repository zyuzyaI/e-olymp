def f(i,n,u):
    
    while True:
        if n<=pow(i,u):
            break
        i+=1
    return i
n=int(input())
i=0
g=0
i=f(i,n,3)
if (i*i*(i-1))>=n:
    if (((i-1)*(i-1)*i)>=n):
        o=i-1
        result=8*o+4+5*o*(o-1)*2+3*(o-1)*2+3*o*(o-1)*(o-1)+2*(o-1)*(o-1)
        p=n-o*o*o
        g=f(g,p,2)
        if (g==1):
            result+=8
        else:
            result+=8+(g-2)*2*5+3*((g-1)*(g-1)-1-(g-2)*2)
        i=1
        while ((g-1)*(g-1)+i <= p):
            if ((i == 1 or i == g) and g != 1):
                result+=5
            else:
                if (g != 1):
                    result+=3
            i+=1    
            
        
    else:
        o=i-1
        result=8*o+4+5*o*(o-1)*2+3*(o-1)*2+3*o*(o-1)*(o-1)+2*(o-1)*(o-1)+o*o*3+5+2*2*(o-1)
        p=n-o*o*(o+1)
        g=f(g,p,2)
        if (g==1):
            result+=8
        else:
            result+=8+(g-2)*2*5+3*((g-1)*(g-1)-1-(g-2)*2)
        i=1
        while ((g-1)*(g-1)+i <= p):
            if ((i == 1 or i == g) and g != 1):
                result+=5
            else:
                if (g != 1):
                    result+=3
            i+=1
else:
    o=i
    result=8*(o-1)+4+5*(o-1)*(o-1)*2+3*(o-1)*2+3*(o-1)*(o-1)*(o-1)+2*(o-1)*(o-1)
    p=n-(o-1)*o*o
    g=f(g,p,2)
    if (g==1):
        result+=8
    else:
        result+=8+(g-2)*2*5+3*((g-1)*(g-1)-1-(g-2)*2)
    i=1
    while ((g-1)*(g-1)+i <= p):
            if ((i == 1 or i == g) and g != 1):
                result+=5
            else:
                if (g != 1):
                    result+=3
            i+=1
            

print(result)