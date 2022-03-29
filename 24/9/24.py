# https://inf-ege.sdamgia.ru/problem?id=27686
with open('24.txt') as F:
    f = F.readline()

    c, cMax = 0, 0
    for i in f:
        if i == 'X':
            c += 1
        else:
            cMax = max(c, cMax)
            c = 0

    print(cMax)
