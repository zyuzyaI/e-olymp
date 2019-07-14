# 8653 Прибавить вычесть и умножить
handle = open("input.txt", "r")
data = (handle.read()).split()
handle.close()
c=1
num=0
for i in range(0,len(data),2):
    if data[i]=='add':
        num+=int(data[c])
        c+=2
    elif data[i]=='subtract':
        num-=int(data[c])
        c+=2
    elif data[i]=='multiply':
        num*=int(data[c])
        c+=2
handl = open("output.txt", "w")
handl.write(str(num))
handl.close()
