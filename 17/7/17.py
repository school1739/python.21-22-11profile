with open('17.txt') as F:
    f = list(map(int, F.readlines()))
    c, cMax = 0, 0
    for i in range(len(f) - 2):
        if f[i] ** 2 + f[i + 1] ** 2 == f[i + 2] ** 2 or \
            f[i + 1] ** 2 + f[i + 2] ** 2 == f[i] ** 2 or \
                f[i] ** 2 + f[i + 2] ** 2 == f[i + 1] ** 2:
            c += 1
            cMax = max(c, f[i] + f[i + 1] + f[i + 2])
    print(c, cMax)
