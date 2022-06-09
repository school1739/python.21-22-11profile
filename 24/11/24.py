with open(r'24.txt') as F:
    f = F.readline()
    f = f.replace('CB', 'AB')
    f = f.replace('AB', 's')

    c = cMax = 0

    for i in f:
        if i == 's':
            c += 1
        else:
            cMax = max(c, cMax)
            c = 0
    print(cMax)
