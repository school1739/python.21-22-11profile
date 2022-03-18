with open('A.txt') as F:
    # f = list(map(int, F.readlines()))
    # f.pop(0)
    n = int(F.readline())
    div19Odd = []
    div19Even = []
    odd = []
    even = []

    # for x in f:
    for i in range(n):
        x = int(F.readline())
        if x % 19 == 0:
            if x % 2 == 0:
                div19Even.append(x)
            else:
                div19Odd.append(x)
        else:
            if x % 2 == 0:
                even.append(x)
            else:
                odd.append(x)

    print(sorted(div19Even)[-2:])
    # print(max(div19Even))
    print(max(div19Odd))
    print(max(even))
    print(max(odd))

    # A
    print('A:', 9918, 9984)
    # print(8455*9918)

    # B
    print('B:', 988, 999)
    # print(8455*9918)

# Ответ: 99189984 988999
