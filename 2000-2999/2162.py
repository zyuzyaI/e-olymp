# 2162 Палиндром
slovo = input()
slovo=''.join(slovo.split())
a = slovo[::-1]
if slovo == a:
  print("YES")
else:
  print("NO")
