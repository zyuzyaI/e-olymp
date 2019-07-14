# 7366 Сколько до Нового Года?
n=int(input())
days=n//86400
n=n%86400
hour=n//3600
n=n%3600
minuts=n//60
n=n%60
print(days, hour, minuts, n)
