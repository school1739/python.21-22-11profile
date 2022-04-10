# https://inf-ege.sdamgia.ru/problem?id=33198

with open('26.txt') as F:
    n, m = map(int, F.readline().split(' '))
    f = list(map(int, F.readlines()))

    c, mass = 0, 0

    rocks = []
    for i in f:
        if 200 <= i <= 210:
            rocks.append(i)
            f.remove(i)

    f = sorted(f)
    for i in f:
        if sum(rocks) + i <= m:
            rocks.append(i)
        else:
            break

    print(len(rocks), sum(rocks))
