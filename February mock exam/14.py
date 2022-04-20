n = 6*512**180+7*64**181+3*8**184+5*8**125-65
s = ''
while n > 0:
    if n % 64 > 9:
        s = '.' + s
    else:
        s = str(n % 64) + s
    n = n//64
print(s)
print(s.count('0'))
