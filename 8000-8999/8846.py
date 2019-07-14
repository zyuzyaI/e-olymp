# 8846 046
n = int(input())
if n < 0:
	n = -n
print(str(n//100)+str(n%10) + str((n//10)%10))
