# https://inf-ege.sdamgia.ru/problem?id=27890

with open('27B.txt') as F:
    n = int(F.readline())

    f = list(map(lambda s: list(map(int, s.split(' '))), F.readlines()))

    minDif, summ = 100000, 0

    for i in f:
        summ += max(i)

        dif = abs(i[0] - i[1])
        if dif != 0 and dif % 5 != 0:
            minDif = min(minDif, dif)

    print(summ, summ % 5, minDif)
