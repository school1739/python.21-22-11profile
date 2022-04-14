# https://inf-ege.sdamgia.ru/problem?id=29675

with open('27B.txt') as F:
    n = F.readline()

    f = list(map(lambda s: list(map(int, s.split(' '))), F.readlines()))

    minDiff = 100000
    summ = 0
    for i in f:
        summ += max(i)
        diff = abs(i[0] - i[1])

        if diff != 0 and diff % 3 == 0:
            minDiff = min(minDiff, diff)
        # if

    print(summ, summ % 3, minDiff, summ - minDiff, (summ - minDiff) % 3)

# 127026
