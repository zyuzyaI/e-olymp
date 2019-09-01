#6975 Магический Множитель
inputfile = open('input.txt', 'r')
for i in inputfile:

	n = int(input())

	def seach_num(num):
		for i in range(10):
			if str(i) not in (num):
				return False

		return True


	str_arr = []
	k = 1
	while True:
		str_arr += str(k * n)
		if seach_num(str_arr):
			print(k)
			break
		k += 1
