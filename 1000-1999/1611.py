# 1611 Реверс подстроки
n=input()
ind=[int(i) for i in (input().split())]
pod=n[ind[0]-1:ind[1]]
spis=n[:ind[0]-1]+pod[::-1]+n[ind[1]:]
print(spis)
