n = int(input())
mass = []
for i in range(n):
	mass.append(input())
counter = 1
i, j = map(int, input().split())
if i != n and j != n:
	if mass[i-2][j-1] == '.':
		counter += 1
	if mass[i-1][j-2] == '.':
		counter += 1
	if mass[i-2][j-2] == '.':
		counter += 1
	if mass[i][j-1] == '.':
		counter += 1
	if mass[i-1][j] == '.':
		counter += 1
	if mass[i][j] == '.':
		counter += 1
else:
	if i == n and j == n:
		if mass[i-2][j-1] == '.':
			counter += 1
		if mass[i-1][j-2] == '.':
			counter += 1
		if mass[i-2][j-2] == '.':
			counter += 1
	else:
		if i == n:
			if mass[i-2][j-1] == '.':
				counter += 1
			if mass[i-1][j-2] == '.':
				counter += 1
			if mass[i-2][j-2] == '.':
				counter += 1
			if mass[i-1][j] == '.':
				counter += 1
		else:
			if mass[i-2][j-1] == '.':
				counter += 1
			if mass[i-1][j-2] == '.':
				counter += 1
			if mass[i-2][j-2] == '.':
				counter += 1
			if mass[i][j-1] == '.':
				counter += 1
			
	
print(counter)


