import math

with open('27A.txt') as F:
    n = F.readline()

    f = list(map(lambda s: list(map(int, s.strip().split(' '))), F.readlines()))

    summ = 0
    minDiff = []
    for i in f:
        lcms = []
        for xi in range(len(i)-1):
            for yi in range(xi + 1, len(i)):
                lcms.append(math.lcm(i[xi], i[yi]))
        m = max(lcms)
        for j in range(len(lcms)):
            lcms[j] = m-lcms[j]
        minDiff.append(lcms)
        summ += m

    print(summ)
    sm = 0
    for i in minDiff:
        for j in i:
            if ((summ-j) % 5 == 0 or (summ-j) % 7 == 0) and (summ-j) % 35 != 0:
                sm = max(sm, summ-j)
    print(sm, sm % 5, sm % 7)
