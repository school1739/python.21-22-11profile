with open('B.txt') as F:
    f = list(map(int, F.readlines()))
    f.pop(0)
    div13Odd = []
    div13Even = []
    odd = []
    even = []

    for x in f:
        if x % 13 == 0:
            if x % 2 == 0:
                div13Even.append(x)
            else:
                div13Odd.append(x)
        else:
            if x % 2 == 0:
                even.append(x)
            else:
                odd.append(x)

    print('div13Odd:', min(div13Odd))
    print('div13Even:', min(div13Even))
    print('odd:', min(odd))
    print('even:', min(even))
    print('')
    print('A:', 6, 637)
    print('B:', 10, 13)

# Ответ: 6637 1013
