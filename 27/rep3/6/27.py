with open('B.txt') as F:
    f = list(map(int, F.readlines()))
    f.pop(0)

    max1, max2 = 0, 0
    remainders = [0] * 120

    # Eсли сумма остатков чисел x и y делится на a
    # (x % a + y % a) % a == 0
    # то и x + y делится на a
    # (x + y) % a == 0

    for x in f:
        if (x + remainders[(120 - (x % 120)) % 120]) > (max1 + max2) and \
                remainders[(120 - (x % 120)) % 120] > x:
            max1, max2 = remainders[(120 - (x % 120)) % 120], x

        # Обновляем список останков новым x
        if x > remainders[x % 120]:
            remainders[x % 120] = x

    print(max1, max2)
    print('A:', 98169984)
    print('B:', 956964)
