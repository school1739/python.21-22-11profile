b = open('24.txt') 
a = b.readlines()
s = a.split('A')

k = 0 
for i in range(1, len(s) - 1):
	if s[i].count('B') >= 2 and len(s[i]) <= 10:
		k += 1
print(k)
	
