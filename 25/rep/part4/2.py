def isSimple(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0 or x % (x//i) == 0:
            return False

    return True


n = 580001
c = 0

while c != 5:
    P = 1
    for i in range(2, int(n**0.5) + 1):
        if i*i == n and (not isSimple(i)):
            P *= i
        elif n % i == 0:
            if not isSimple(i):
                P *= i
            if not isSimple(n//i):
                P *= n//i

    if P % 10 == 9:
        print(n, P)
        c += 1

    n += 1
# Ответ
# 580017 336419720289
# 580027 38079326761177248071621220583780489
# 580047 38087205554983716487188457403575329
# 580053 336461482809
# 580057 336466123249
