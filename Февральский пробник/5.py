for n in range(1000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = r + bin(r.count('1'))[2:]
    else:
        r = '1' + r + '00'
    if int(r, 2) > 215:
        print(n)
        break
