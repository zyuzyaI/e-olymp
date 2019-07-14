# 8954 154
n = int(input())
s = []
for i in range(n):
	s.append(int(input()))

print(*s[::-1])
