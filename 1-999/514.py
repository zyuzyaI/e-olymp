# 514 Время для Николая
n=(input().split())
T1=n[0].split(':')
T2=n[1].split(':')
t1=int(T1[0])*3600+int(T1[1])*60+int(T1[2])
t2=int(T2[0])*3600+int(T2[1])*60+int(T2[2])
d = (t2-t1+3600*24)%(3600*24)
h3 =str(int(d/3600))
d=d%3600
m3=str(int(d/60))
s3=str(int(d%60))
h3=h3 if len(h3)==2 else '0'+h3
s3=s3 if len(s3)==2 else '0'+s3
m3=m3 if len(m3)==2 else '0'+m3
print(h3, m3, s3,sep=':')
