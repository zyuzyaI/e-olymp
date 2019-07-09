# 1124 Алфавитное граффити
n=int(input())
d=('abcdefghijklmnopqrstuvwxyz')
for i in range(1,n+1):
    print('a'+(n-i)*' '+str(d[:i]))
