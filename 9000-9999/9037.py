# Удаление цифр
def max_n(n):
	n = str(n)
	return max(int(i) for i in n)



n = int(input())
counter = 1
while len(str(n)) != 1:
	n = str(int(n) - max_n(n))
	counter += 1
print(counter)
