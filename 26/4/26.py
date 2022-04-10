# https://inf-ege.sdamgia.ru/problem?id=33528

with open('26.txt') as F:

    n, m = map(int, F.readline().split(' '))
    f = list(map(lambda l: l.strip(), F.readlines()))
    aMatrix = []
    bMatrix = []

    for i in f:
        x, y = map(int, i.split(' ')[:2])
        z = i.split(' ')[-1]

        if z == 'A':
            aMatrix.append([x, y])
        else:
            bMatrix.append([x, y])

    bMatrix = sorted(bMatrix)

    aSum = 0
    for i in aMatrix:
        aSum += i[0] * i[1]

    m -= aSum
    c = 0
    for i in bMatrix:
        fl = False
        for j in range(i[1]):
            buffer = i[0]
            if m - buffer >= 0:
                m -= buffer
                c += 1
            else:
                fl = True
                break
        if fl:
            break

    print(c, m)
