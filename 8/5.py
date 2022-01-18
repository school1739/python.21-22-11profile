num = 36**9 + 6**25 - 9

s = ''
while num > 0:
    s = str(num % 6) + s
    num //= 6

print(s)
print(s.count('0'))
