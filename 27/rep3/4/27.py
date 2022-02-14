with open('A.txt') as F:
    f = list(map(int, F.readlines()))
    f.pop(0)

    div21 = []
    div7 = []
    div3 = []
    nondiv = []

    for x in f:
        if x % 21 == 0:
            div21.append(x)
        elif x % 7 == 0:
            div7.append(x)
        elif x % 3 == 0:
            div3.append(x)
        else:
            nondiv.append(x)

    print('div21:', sorted(div21)[-2:])
    print('div7:', max(div7))
    print('div3:', max(div3))
    print('nondiv:', max(nondiv))
    print('')
    print('A:', 9947*9984)
