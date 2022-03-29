num = ('Число')
base =  ('Система счисления')
newnum = ""
while num>0:
	newnum = str(num % base	) + newnum
	num //= base
print(newnum)

