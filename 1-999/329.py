# 329 Количество слов
n=input()
n=n.replace(' - ', ' ')
n=n.replace('-','')
n=n.replace('_', '')
n=n.replace("'",'')
a=n.split()

c=len(a)
print(c)
