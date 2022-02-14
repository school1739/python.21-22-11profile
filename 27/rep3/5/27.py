with open('B.txt') as F:
    f = list(map(int, F.readlines()))
    f.pop(0)

    div7 = []
    none = []

    for x in f:
        if x % 7 == 0:
            div7.append(x)
        else:
            none.append(x)

    div7.sort()
    none.sort()

    print(div7[-2:])
    print(none[-2:])
    print('')
    print('A:', 99479984)
    print('B:', 994999)
