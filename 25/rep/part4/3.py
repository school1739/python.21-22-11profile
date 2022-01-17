def isSimple(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0 and x % (x//i) == 0:
            return False

    return True


c = 0
n = 250001
while c != 5:
    S = 0
    for i in range(2, int(n ** 0.5) + 1):
        if i * i == n:
            if isSimple(i):
                S += i
        elif n % i == 0:
            if isSimple(i):
                S += i
            if isSimple(n//i):
                S += n//i

    if S != 0 and S % 25 == 0:
        print(n, S)
        c += 1
    n += 1

# Ответ
# 250081 19250
# 250108 2050
# 250111 3800
# 250129 22750
# 250139 8100
